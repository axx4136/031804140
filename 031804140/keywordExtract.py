import re
import jieba.analyse
import math
import numpy as np
import time
import sys
def keywordExtract(txt):
    Word_dictionary={}
    key_word = jieba.analyse.extract_tags(txt, topK=20, withWeight=True)
    # 删除前三高权重的关键词
    for i in range(0,3):
        del key_word[0]
    # 将列表转为字典
    for key,value in key_word:
        Word_dictionary[key]=value
    return Word_dictionary