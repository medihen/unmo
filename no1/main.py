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
        'what'Responderインスタンスを生成し、保持する。
        """
        self._name = name
        self._responder = Responder('what')

    def dialogue(self, text):
        """
        ユーザからの入力を受け取り、Responderに処理させた結果を返す。
        """
        return self._responder.response(text)

    @property
    def name(self):
        """人工無脳インスタンスの名前"""
        return self._name

    @property
    def responder_name(self):
        """保持しているResponderの名前"""
        return self._responder.name

def build_prompt(unmo):
    """
    AIインスタンスを取り、AIとResponderの名前を整形して返す
    """
    return '{name}:{responder}> '.format(name=unmo.name,
                                       responder=unmo.responder_name)

if __name__=='__main__':
    print('Unmo System prototype : proto')
    proto= Unmo('proto')
    while True:
        text = input('> ')
        if not text:
            break

        response = proto.dialogue(text)
        print('{prompt}{response}'.format(prompt=build_prompt(proto),
                                          response=response))
