import re
import jieba.analyse
import math
import numpy as np
import time
import sys
def Format(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as f:
            result = f.read()
            #sub用空字符替换标点符号
            result = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）：]+", "", result)
    except:
        print("读取失败")
    return result