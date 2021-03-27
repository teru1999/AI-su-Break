# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
from gensim.models import word2vec

def main(kw):
    keyword = kw
    finpath = 'rsc/tmp/talk.txt'  # 元コーパス
    foutpath = 'rsc/corpus/corpus.txt'
    model_name = 'rsc/corpus/testmodel'

    # file操作
    f = open(finpath, 'r', encoding='UTF-8')
    text = f.read()
    f.close()

    # wakatiにしてfile保存
    t = Tokenizer()
    l = list(t.tokenize(text, wakati=True))
    s = ''

    for item in l:
        s += (item + ' ')
        
    fo = open(foutpath, 'w', encoding='UTF-8')
    fo.write(s)
    fo.close()

    # word2vec
    sentences = word2vec.LineSentence(foutpath)
    model = word2vec.Word2Vec(sentences,
                            sg=1,
                            size=100,
                            min_count=1,
                            window=10,
                            hs=1,
                            negative=0)

    model.save(model_name)

    model   = word2vec.Word2Vec.load(model_name)
    results = model.most_similar(positive = keyword, topn=3)
    for result in results:
        print(result[0], '\t', result[1])


if __name__ == '__main__':
    main()