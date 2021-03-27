# coding: utf-8
from janome.tokenizer import Tokenizer
import collections

def main(inf):
    f = open(inf, 'r', encoding='UTF-8')
    text = f.read()
    t = Tokenizer()

    # 単語頻度
    # c = collections.Counter(t.tokenize(text, wakati=True))
    # print(c.most_common()[:15])

    # 特定の品詞のみ
    c = collections.Counter(token.base_form for token in t.tokenize(text) if token.part_of_speech.startswith('名詞'))
    # print(c.most_common()[:15])

    f.close()

    return c.most_common()[0][0]

if __name__ == '__main__':
    main('../rsc/stream20210327-141748.txt')