import functools
import json
from pypinyin import pinyin, lazy_pinyin, Style

with open('result_v1.json', 'r') as f:
    rhyme_dict = json.load(f)

new_rhyme_dict = {}

for k in rhyme_dict:
    for word in rhyme_dict[k]:
        py = pinyin(word, style=Style.FINALS, errors='ignore')
        key = functools.reduce(lambda a, b : a + b, py)
        lw = lazy_pinyin(word)
        if len(key) == len(lw):
            for i, w in enumerate(lw):
                if w in ['ri', 'zhi', 'chi', 'shi', 'zi', 'ci', 'si']:
                    key[i] = 'ri'
        key = '-'.join(key)
        if key not in new_rhyme_dict:
            new_rhyme_dict[key] = [word]
        else:
            if word not in new_rhyme_dict[key]:
                new_rhyme_dict[key].append(word)

with open('result.json', 'w') as fp:
    json.dump(new_rhyme_dict, fp)
