#coding: utf-8
import pandas as pd,numpy as np
from datetime import *
"""
对比 python IO还有pandas的Io
"""
s1=datetime.now()

df=pd.read_csv("D:\\workspace\\kdd 2015\\train\\log_train.csv",chunksize=10)   #0.003s 读取800万条数据，python需要 3s，r需要1分钟

# fid=open("D:\\workspace\\kdd 2015\\train\\log_train.csv")
# entrys=fid.readlines()[1:]

print datetime.now()-s1
print df
