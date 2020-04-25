import re

def find_chinese(words):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', words)
    return chinese
