# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

import re
from janome.tokenizer import Tokenizer

class Dictionary:
    """
    思考エンジンのクラス。

    クラス変数:
    DICT_RANDOM -- ランダム辞書のファイル名。
    DICT_PATTERN -- パターン辞書のファイル名。
    TOKENIZER -- 形態素解析ツールjanomeの分析オブジェクト

    プロパティ:
    random -- ランダム辞書
    pattern -- パターン辞書
    """

    DICT_RANDOM = 'dics/random.txt'
    DICT_PATTERN = 'dics/pattern.txt'

    TOKENIZER = Tokenizer()

    def __init__(self):
        """
        ファイルからの辞書の読み込みを行う。
        """
        with open(Dictionary.DICT_RANDOM, encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        with open(Dictionary.DICT_PATTERN, encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

    def study(self, text):
        """
        ランダム辞書、パターン辞書をメモリに保存する。
        """
        self.study_random(text)
        self.study_pattern(text, Dictionary.analyze(text))

    def study_random(self, text):
        """
        ユーザの発言textをメモリに保存する。
        すでに同じ発言があった場合は何もしない。
        """
        if not text in self._random:
            self._random.append(text)

    def study_pattern(self, text, parts):
        """
        ユーザの発言textを形態素partsに基づいてパターン辞書に保存する。
        """
        for word, part in parts:
            if self.is_keyword(part): # 品詞が名詞であれば学習。
                # 単語の重複チェック
                # 同じ単語で登録されていれば、パターンを追加する
                # 無ければ新しいパターンを作成する
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                if duplicated:
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                else:
                    self._pattern.append({'pattern': word, 'phrases': [text]})

    def save(self):
        """
        メモリ上の辞書をファイルに保存する。
        """
        with open(Dictionary.DICT_RANDOM, mode='w', encoding='utf-8') as f:
            f.write('\n'.join(self.random))

    @staticmethod
    def make_pattern(line):
        """
        文字列lineを\tで分割し、{'pattern':[0], 'pharases':[1]}の形式で返す。
        """
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            return {'pattern': pattern, 'phrases': phrases.split('|')}

    @staticmethod
    def analyze(text):
        """
        文字列を形態素解析し、[(surface, parts)]の形にして返す。
        """
        return [(t.surface, t.part_of_speech) for t in Dictionary.TOKENIZER.tokenize(text)]

    @staticmethod
    def pattern_to_line(pattern):
        """
        パターンのハッシュを文字列に変換する。
        """
        return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

    @staticmethod
    def is_keyword(part):
        """
        品詞partが学習すべきキーワードであるかどうか真偽値で返す。
        """
        return bool(re.match(r'名詞,(一般|代名詞|固有名詞|サ変接続|形容動詞語幹)', part))

    @property
    def random(self):
        """
        ランダム辞書
        """
        return self._random

    @property
    def pattern(self):
        """
        パターン辞書
        """
        return self._pattern
