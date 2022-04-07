# coding=UTF-8

import jieba
from gensim.models import Doc2Vec
import pandas as pd
from member1.config import Config
from tqdm import tqdm

"""job_description embeding"""
s2vectors=Doc2Vec.load(Config.doc2vec_path + "/d2v100.model")
jods_desc = pd.read_csv(Config.jods_desc_path)

jods_desc = list(jods_desc["0"])
doc2vec = []
for jod_desc in tqdm(jods_desc):
    vec = s2vectors.infer_vector(jieba.lcut(jod_desc, cut_all=False))
    doc2vec.append(vec)

dic = {"job_description":jods_desc,
       "word_vec":doc2vec}
df = pd.DataFrame(dic)
df.to_csv(Config.embeding_path+"/job_description.csv", index=None)

"""job_title embeding"""
s2vectors=Doc2Vec.load(Config.doc2vec_path + "/d2v100_jd_title.model")
jds_title = pd.read_csv(Config.jds_title_path)
jds_title = list(jds_title["jd_title"])
doc2vec = []
for jd_title in tqdm(jds_title):
    vec = s2vectors.infer_vector(jieba.lcut(jd_title, cut_all=False))
    doc2vec.append(vec)

dic = {"jd_title":jds_title,
       "word_vec":doc2vec}
df = pd.DataFrame(dic)
df.to_csv(Config.embeding_path+"/jd_title.csv", index=None)
