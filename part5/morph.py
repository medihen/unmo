# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

import re
from janome.tokenizer import Tokenizer

TOKENIZER = Tokenizer()

def analyze(text):
    """
    文字列を形態素解析し、[(surface, parts)]の形にして返す。
    """
    return [(t.surface, t.part_of_speech) for t in TOKENIZER.tokenize(text)]

def is_keyword(part):
    """
    品詞partが学習すべきキーワードであるかどうか真偽値で返す。
    """
    return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)', part))
