# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

import re
from random import choice

class Responder:
    """
    AIの応答を制御する思考エンジンの基底クラス。
    継承して使わなければならない。

    メソッド:
    response(str) -- ユーザの入力

    プロパティ：
    name -- Responderオブジェクトの名前
    """

    def __init__(self, name, dictionary):
        """文字列を受け取り、自身のnameに設定する。"""
        self._name = name
        self._dictionary = dictionary

    def response(self, text):
        """文字列を受け取り、思考した結果を返す。"""
        pass

    @property
    def name(self):
        """思考エンジンの名前"""
        return self._name


class WhatResponder(Responder):
    """ AIの応答を制御する思考エンジンクラス
        入力に対して疑問形で聞き返す。
    """

    def response(self, text):
        """ユーザから入力(text)を受け取り、AIの応答を生成して返す。"""
        return '{}ってなに？'.format(text)


class RandomResponder(Responder):
    """
    AIの応答を制御する思考エンジンクラス。
    登録された文字列からランダムなものを返す。

    クラス変数:
    RESPONSES -- 応答する文字列のリスト
    """

    def __init__(self, name, dictionary):
        """
        文字列nameを受け取り、オブジェクトの名前に設定する。
        'dics/random.txt'ファイルから応答文字列のリストを読み込む。
        """
        super().__init__(name, dictionary)
        with open('dics/random.txt', mode='r', encoding='utf-8') as f:
            self._responses = [x for x in f.read().splitlines() if x]

    def response(self, _):
        """ユーザからの入力は受け取るが、使用せずにランダムな応答を返す"""
        return choice(self._responses)

class PatternResponder(Responder):
    """
    AIの応答を制御する思考エンジンクラス。
    登録されたパターンに反応し、関連する応答を返す。
    """

    def response(self, text):
        """
        ユーザの入力に合致するパターンがあれば、関連するフレーズを返す。
        """
        for ptn in self._dictionary.pattern:
            matcher = re.match(ptn['pattern'], text)
            if matcher:
                chosen_response = choice(ptn['phrases'])
                return chosen_response.replace('%match%', matcher[0])
        return choice(self._dictionary.random)
