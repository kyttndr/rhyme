import re
import functools
from pypinyin import pinyin, lazy_pinyin, Style

def find_chinese(words):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', words)
    return chinese

def get_pinyin_key(words):
    py = pinyin(words, style=Style.FINALS, errors='ignore')
    key = functools.reduce(lambda a, b : a + b, py)
    lw = lazy_pinyin(words)
    if len(key) == len(lw):
        for i, w in enumerate(lw):
            if w in ['ri', 'zhi', 'chi', 'shi']:
                key[i] = 'ri'
    key = '-'.join(key)
    return key
