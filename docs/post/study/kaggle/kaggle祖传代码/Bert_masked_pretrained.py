import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
import os
from tokenizers import Tokenizer
from tokenizers.models import BPE,WordLevel
import utils
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertForSequenceClassification, AutoModelForMaskedLM, BertModel
from transformers import DataCollatorForLanguageModeling
from transformers import RobertaConfig
from transformers import RobertaForMaskedLM,AlbertForMaskedLM,XLNetLMHeadModel
from transformers import Trainer, TrainingArguments

import torch

class TrainDataset:
    def __init__(self, features):
        self.features = features
        #self.targets = targets

    def __len__(self):
        return len(self.features["input_ids"])

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]).to("cpu") for key, val in self.features.items()}
        return item




class BertPretrain_Masked:
    def __init__(self, data_path='/mnt/atec/train.jsonl',
                 result_path='result.json',
                 output_model_path="trained_models/Bert_second_train",
                 load_model_path="trained_models"):
        self.data_path = data_path
        self.result_path = result_path
        self.output_model_path = output_model_path
        self.load_model_path = load_model_path 
    def train(self):
        df = utils.load_preprocessing_pandas_data(self.data_path)

        train_x, test_x, train_y, test_y = train_test_split(df, df["label"], test_size=0.2, random_state=2019)


        tokenizer = AutoTokenizer.from_pretrained(os.path.join(self.load_model_path,"bert"), do_lower_case=False)
        model = AutoModelForMaskedLM.from_pretrained(os.path.join(self.load_model_path,"bert"), num_labels=2)
        tokenizer.mask_token = '[MASK]'
        tokenizer.pad_token='[PAD]'
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=tokenizer, mlm=True, mlm_probability=0.15 #mlm表示是否使用masked language model；mlm_probability表示mask的几率
        )

        pt_batch = tokenizer(train_x["memo_polish"].values.tolist(), truncation=True, max_length=55)
        dataset = TrainDataset(pt_batch)   
        
        
        training_args = TrainingArguments(
            output_dir=self.output_model_path,
            overwrite_output_dir=True,
            num_train_epochs=3, #训练epoch次数
            per_gpu_train_batch_size=12, #训练时的batchsize
            save_steps=10_000, #每10000步保存一次模型
            save_total_limit=2,#最多保存两次模型
            prediction_loss_only=True,
        )
        trainer = Trainer(
            model=model,
            args=training_args,
            data_collator=data_collator, #数据收集器在这里
            train_dataset=dataset #注意这里选择的是预处理后的数据集
        )

        #开始训练
        trainer.train()
        #保存模型
        trainer.save_model(self.output_model_path)
        #print(trainer.predict(dataset))
        #print("")


if __name__ == '__main__':
    bpm = BertPretrain_Masked(data_path="train_random_data.jsonl")
    bpm.train()