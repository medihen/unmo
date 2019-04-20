# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

from random import choice
from responder import RandomResponder, WhatResponder, PatternResponder
from dictionary import Dictionary

class Unmo:
    """
    人工無脳コアクラス

    プロパティ:
    name -- 人工無脳コアの名前
    responder_name -- 現在の応答(Responder)クラスの名前
    """

    def __init__(self, name):
        """
        文字列を受け取り、コアインスタンスの名前に設定する。
        Responder(What, Random, Pattern)インスタンスを生成し、保持する。
        Dictionaryインスタンスを作成し、保持する。
        """
        self._dictionary = Dictionary()
        
        self._responders = {
            'what':     WhatResponder('What', self._dictionary),
            'random':   RandomResponder('Random', self._dictionary),
            'pattern':  PatternResponder('Pattern', self._dictionary),
        }
        self._name = name
        self._responder = self._responders['pattern']

    def dialogue(self, text):
        """
        ユーザからの入力を受け取り、Responderに処理させた結果を返す。
        呼び出されるたびにランダムでResponderを切り替える。
        """
        chosen_key = choice(list(self._responders.keys()))
        self._responder = self._responders[chosen_key]
        return self._responder.response(text)

    @property
    def name(self):
        """人工無脳インスタンスの名前"""
        return self._name

    @property
    def responder_name(self):
        """保持しているResponderの名前"""
        return self._responder.name
