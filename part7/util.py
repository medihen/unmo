# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

def format_error(error):
    """
    例外errorを受け取り、'名前: メッセージ'の形で返す。
    """
    return '{}: {}'.format(type(error).__name__, str(error))
