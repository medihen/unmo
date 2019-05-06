# Python初心者に送る「人工知能の作り方」
# http://sandmark.hateblo.jp/entry/2017/10/07/141339
# に掲載されたコードを写経して勉強する。

import os.path
from collections import defaultdict
import morph

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
    template -- テンプレート辞書
    """

    DICT = {'random': 'dics/random.txt',
            'pattern': 'dics/pattern.txt',
            'template': 'dics/template.txt',
            }

    def __init__(self):
        """
        ファイルからの辞書の読み込みを行う。
        """
        Dictionary.touch_dics()
        with open(Dictionary.DICT['random'], encoding='utf-8') as f:
            self._random = [x for x in f.read().splitlines() if x]

        with open(Dictionary.DICT['pattern'], encoding='utf-8') as f:
            self._pattern = [Dictionary.make_pattern(l) for l in f.read().splitlines() if l]

        with open(Dictionary.DICT['template'], encoding='utf-8') as f:
            self._template = defaultdict(lambda: [], {})
            for line in f:
                count, template = line.strip().split('\t')
                if count and template:
                    count = int(count)
                    self._template[count].append(template)

    def study(self, text, parts):
        """
        ランダム辞書、パターン辞書、テンプレート辞書をメモリに保存する。
        """
        self.study_random(text)
        self.study_pattern(text, parts)
        self.study_template(parts)

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
            if morph.is_keyword(part): # 品詞が名詞であれば学習。
                # 単語の重複チェック
                # 同じ単語で登録されていれば、パターンを追加する
                # 無ければ新しいパターンを作成する
                duplicated = next((p for p in self._pattern if p['pattern'] == word), None)
                if duplicated:
                    if not text in duplicated['phrases']:
                        duplicated['phrases'].append(text)
                else:
                    self._pattern.append({'pattern': word, 'phrases': [text]})

    def study_template(self, parts):
        """
        形態素のリストpartsを受け取り、
        名詞のみ'%noun%'に変更した文字列templateをself._templateに追加する。
        名詞が存在しなかった場合、また同じtempkateが存在する場合何もしない。
        """
        template = ''
        count = 0
        for word, part in parts:
            if morph.is_keyword(part):
                word = '%noun%'
                count += 1
            template += word

        if count > 0 and template not in self._template[count]:
            self._template[count].append(template)

    def save(self):
        """
        メモリ上の辞書をファイルに保存する。
        """
        with open(Dictionary.DICT['random'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join(self.random))

        with open(Dictionary.DICT['pattern'], mode='w', encoding='utf-8') as f:
            f.write('\n'.join([Dictionary.pattern_to_line(p) for p in self._pattern]))

        with open(Dictionary.DICT['template'], mode='w', encoding='utf-8') as f:
            for count, templates in self._template.items():
                for template in templates:
                    f.write('{}\t{}\n'.format(count, template))


    @staticmethod
    def make_pattern(line):
        """
        文字列lineを\tで分割し、{'pattern':[0], 'pharases':[1]}の形式で返す。
        """
        pattern, phrases = line.split('\t')
        if pattern and phrases:
            return {'pattern': pattern, 'phrases': phrases.split('|')}

    @staticmethod
    def pattern_to_line(pattern):
        """
        パターンのハッシュを文字列に変換する。
        """
        return '{}\t{}'.format(pattern['pattern'], '|'.join(pattern['phrases']))

    @staticmethod
    def touch_dics():
        for dic in Dictionary.DICT.values():
            if not os.path.exists(dic):
                open(dic, 'w').close()

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

    @property
    def template(self):
        """
        テンプレート辞書
        """
        return self._template
