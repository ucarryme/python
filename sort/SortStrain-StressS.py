#该程序处理同一变形量和压缩速率下不同温度的应力应变曲线
#预处理：删除应力应变前部分的正值和减序的应力应变数据（如没有则跳过），在将所有数值取绝对值，尾部数据选择处理


import math
from numpy import NaN
import pandas as pd
#文件路径和文件名
path = 'E:/4130x-GLEEBLE/data/10/10+30%/fix/'
filename = "10+30%+T1.xlsx"
df = pd.read_excel(path+filename)

#列名index；自定义格式化
ColName = ["True Strain900","True Strain950","True Strain1000","True Strain1050","True Strain1100","True Strain1200"]
Col2Name = ["True Stress900","True Stress950","True Stress1000","True Stress1050","True Stress1100","True Stress1200"]
dataArr = []
fixedStrain = pd.DataFrame()
dataFrame = pd.DataFrame()

for i in range(len(ColName)):
    for j in range(len(df)):
        if j ==len(df) -1 or math.isnan(df[ColName[i]][j+1]) :
            break       
        if df[ColName[i]][j] > 0:
            df[ColName[i]][j]  =  NaN
            df[Col2Name[i]][j]  =  NaN
            continue
       
        if ((math.fabs(df[ColName[i]][j]) > math.fabs(df[ColName[i]][j+1]))):
            df[ColName[i]][j]  =  NaN
            df[Col2Name[i]][j]  =  NaN
            continue
         

for i in range(len(ColName)):
    for j in range(len(df)):
        df[ColName[i]][j]  =  df[ColName[i]][j]*-1
        df[Col2Name[i]][j]  = df[Col2Name[i]][j]*-1






            
   


        
    



index = 0
#将每组的应变部分实现左移至0开始，且与对应应力部分匹配装入dataframe类
for i in range(len(ColName)):
    for j in range(len(df)):
        if math.isnan(df[ColName[i]][j]) == False:
            index = j
            temp = df[ColName[i]]-df[ColName[i]][j]
    dataArr.append(temp)
    fixedStrain = pd.concat([fixedStrain,dataArr[i],df[Col2Name[i]]],axis= 1)

#生成execl文件
fixedStrain.to_excel(path+'fixedStrainData.xlsx')

