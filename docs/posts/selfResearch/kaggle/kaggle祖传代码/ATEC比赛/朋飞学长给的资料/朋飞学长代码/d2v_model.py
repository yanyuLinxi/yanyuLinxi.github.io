# coding=UTF-8

from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from member1.config import Config
import jieba

"""jd_title model"""
f = open(Config.embeding_doc_path + "/jd_title.txt", encoding='utf8', errors='ignore')
sentences = f.read().strip().split("\n")
j = 0
for i in range(len(sentences)):
    j += 1
    if j % 1000 == 0:
        print(j)
    sentences[i] = jieba.lcut(sentences[i],cut_all=False)

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(sentences)]
model = Doc2Vec(documents, dm=1, vector_size=100, window=8, min_count=5, workers=4)
model.save(Config.doc2vec_path + "/d2v100_jd_title.model")

"""job_desc model"""
f = open(Config.embeding_doc_path + "/job_desc.txt", encoding='utf8', errors='ignore')
sentences = f.read().strip().split("\n")
j = 0
for i in range(len(sentences)):
    j += 1
    if j % 1000 == 0:
        print(j)
    sentences[i] = jieba.lcut(sentences[i],cut_all=False)

documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(sentences)]
model = Doc2Vec(documents, dm=1, vector_size=100, window=8, min_count=5, workers=4)
model.save(Config.doc2vec_path + "/d2v100.model")

