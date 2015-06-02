#coding: utf-8
import numpy as np,pandas as pd,cPickle as pickle,time,re
from datetime import *

"""
log_train_clean，保存clean后的结果，分别是：enrollment_id，time，source，event，object
object，source，event都要映射成数字，time保存的是2000,1,1日0,0,0秒,的偏移值
source：server=1 , browser=2
event：
  1. problem - Working on course assignments.
  2. video - Watching course videos.
  3. access - Accessing other course objects except videos and assignments.
  4. wiki - Accessing the course wiki.
  5. discussion - Accessing the course forum.
  6. navigate - Navigating to other part of the course.
  7. page_close – Closing the web page.
"""
dir_kdd="D:\\workspace\\kdd 2015\\"

def change2CSV(dataAry,fileName,columns):    #column 是每列header的名称,list型
    filePath=dir_kdd + "data_clean\\" + fileName
    dd=pd.DataFrame(dataAry,columns=columns)
    dd.to_csv(filePath+".csv",header=True,index=False)

def index_log_train(fileName):
    ss=datetime.now()
    fid=open(dir_kdd + "train\\" + fileName+".csv")                        # enrollment_id , username , course_id
    eventList=["problem",
               "video",
                "access",
               "wiki",
               "discussion",
               "nagivate",
               "page_close"]
    lineNo , obj_no = 0 , 0                          #第一行是header
    obj ,log_train_clean , oTime = [] , np.zeros((8157277,5),dtype=int) , datetime(2000,1,1,0,0,0)
    entrys=fid.readlines()[1:]
    ee=datetime.now()
    print ee-ss
    for line in entrys:
        line2list=line.strip().split(",")                           #分解原始字符串
        if len(line2list)!=5:print line                             #异常输出
        log_train_clean[lineNo][0] = int(line2list[0])              #enrollment_id
        curTimeList=[int(i) for i in re.split("[T , \- , :]",line2list[1])]         #分解时间字符串，并转为 numeric型
        curTime=datetime(curTimeList[0],curTimeList[1],curTimeList[2],curTimeList[3],curTimeList[4],curTimeList[5])
        log_train_clean[lineNo][1] = (curTime-oTime).total_seconds()
        log_train_clean[lineNo][2] = 1 if line2list[2]=="server" else 2      #source
        log_train_clean[lineNo][3] = eventList.index(line2list[3])+1        #event

        if line2list[4] not in obj:
            obj.append(line2list[4])
            log_train_clean[lineNo][4]=obj_no
            obj_no+=1
        else:
            log_train_clean[lineNo][4]=obj.index(line2list[4])
        lineNo+=1
        print lineNo
    pickle.dump(log_train_clean,open(dir_kdd+"data_clean//tmpLogTrain",'w'))
    pickle.dump(obj,open(dir_kdd+"data_clean//tmpobj",'w'))
    log_train_columns=["enrollment_id" , "time" , "source" , "event" , "object"]
    change2CSV(log_train_clean,fileName,log_train_columns)
    objColumns=["objectString"]
    change2CSV(obj,"objectString",objColumns)


if __name__=="__main__":
    index_log_train("log_train")


