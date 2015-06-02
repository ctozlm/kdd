#coding: utf-8
import numpy as np,pandas as pd

"""
username , course_id 要映射成数字
enrollment_clean   保存clean后的数据，分别是 enrollment_id , username ,course_id
"""

dir_kdd="D:\\workspace\\kdd 2015\\"

def change2CSV(dataAry,fileName,columns):    #column 是每列header的名称,list型
    filePath=dir_kdd + "data_clean\\" + fileName
    dd=pd.DataFrame(dataAry,columns=columns)
    dd.to_csv(filePath+".csv",header=True,index=False)

def index_enrollment_train(fileName):
    fid=open(dir_kdd + "train\\" + fileName)                        # enrollment_id , username , course_id
    lineNo , uno , cno = 0 , 0 , 0
    user , course ,enrollment_clean= [] , [] , np.zeros((120542,3),dtype=int)
    entrys=fid.readlines()[1:]
    for line in entrys:
        line2list=line.strip().split(",")
        enrollment_clean[lineNo][0]=int(line2list[0])          #enrollment_id
        if line2list[1] not in user:
            user.append(line2list[1])
            enrollment_clean[lineNo][1]=uno
            uno+=1
        else:
            enrollment_clean[lineNo][1]=user.index(line2list[1])
        if line2list[2] not in course:
            course.append(line2list[2])
            enrollment_clean[lineNo][2]=cno
            cno+=1
        else:
            enrollment_clean[lineNo][2]=course.index(line2list[2])
        lineNo+=1
    enrollment_columns=["enrollment_id" , "username" , "course_id" ]
    change2CSV(enrollment_clean,fileName,enrollment_columns)
    userColumns=["userString"]
    change2CSV(user,"userString",userColumns)
    courseColumns=["courseString"]
    change2CSV(course,"courseString",courseColumns)

if __name__=="__main__":
    index_enrollment_train("enrollment_train.csv")