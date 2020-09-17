import re
import jieba.analyse
import math
import numpy as np
import time
import sys
def cosinSimilarity(vector_origin,vector_fake,path_origin,path_fake):
    # 字典合并过程
    for key in vector_origin:
        vector_fake[key]=vector_fake.get(key,0)
    for key in vector_fake:
        vector_origin[key]=vector_origin.get(key,0)
    # 余弦相似度再现
    sum = 0
    sq1 = 0
    sq2 = 0
    for key in vector_origin:
        sum += vector_origin[key] * vector_fake[key]
        sq1 += pow(vector_origin.get(key,0), 2)
        sq2 += pow(vector_fake.get(key,0), 2)
    cosans = round((float(sum) / (math.sqrt(sq1) * math.sqrt(sq2))), 2)
    return cosans