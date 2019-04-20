# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

class Dictionary:
    """
    思考エンジンのクラス。

    クラス変数:
    DICT_RANDOM -- ランダム辞書のファイル名。
    DICT_PATTERN -- パターン辞書のファイル名。

    プロパティ:
    random -- ランダム辞書
    pattern -- パターン辞書
    """

    DICT_RANDOM = 'dics/random.txt'
    DICT_PATTERN = 'dics/pattern.txt'

    def __init__(self):
        """
        ファイルからの辞書の読み込みを行う。
        """
        with open(Dictionary.DICT_RANDOM, encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        with open(Dictionary.DICT_PATTERN, encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

    @staticmethod
    def make_pattern(line):
        """
        文字列lineを\tで分割し、{'pattern':[0], 'pharases':[1]}の形式で返す。
        """
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            return {'pattern': pattern, 'phrases': phrases.split('|')}

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
