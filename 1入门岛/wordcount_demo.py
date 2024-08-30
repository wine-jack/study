import re
from collections import Counter

def wordcount(text):
    # 使用正则表达式移除非字母字符，并将所有字符转换为小写
    words = re.findall(r'\b\w+\b', text.lower())
    # 使用Counter来统计单词出现的次数
    return Counter(words)

# 给定的文本
text = """
Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.
"""

# 调用wordcount函数
word_counts = wordcount(text)

# 打印结果
for key, value in word_counts.items():
    print(f"'{key}': {value}")