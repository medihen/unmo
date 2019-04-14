# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

class Responder:
    """ AIの応答をコントロールするクラス

    プロパティ：
    name -- Responderオブジェクトの名前
    """

    def __init__(self, name):
        """文字列を受け取り、自身のnameに設定する。"""
        self._name = name

    def response(self, text):
        """ユーザから入力(text)を受け取り、AIの応答を生成して返す。"""
        return '{}ってなに？'.format(text)

    @property
    def name(self):
        """応答オブジェクトの名前"""
        return self._name
