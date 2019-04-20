# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

from unmo import Unmo

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
