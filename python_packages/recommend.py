# -*- coding: utf-8 -*- 
from gensim.models import word2vec

def main(kw):
    keyword = kw
    model_name = 'rsc/corpus/testmodel'

    model   = word2vec.Word2Vec.load(model_name)

    results = model.most_similar(positive = keyword, topn=10)

    # for result in results:
    #     print(result[0], '\t', result[1])

    model_name = '../rsc/corpus/testmodel'
    return results