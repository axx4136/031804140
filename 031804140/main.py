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
            # sub用空字符替换标点符号
            result = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）：]+", "", result)
    #如果路径名无效或文件名不匹配
    except:
        print("读取失败")
    return result
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
#命令行获取绝对路径
originFilePath=sys.argv[1]
fakeFilePath=sys.argv[2]
outputFilePath=sys.argv[3]
inputFile_origin=Format(originFilePath)
inputFile_fake = Format(fakeFilePath)
ans=cosinSimilarity(keywordExtract(inputFile_origin),keywordExtract(inputFile_fake),originFilePath,fakeFilePath)
#以字符串形式写入
ans=str(ans)
outputfile = open(outputFilePath, 'w', encoding='utf-8')
outputfile.write(ans)
outputfile.close()




