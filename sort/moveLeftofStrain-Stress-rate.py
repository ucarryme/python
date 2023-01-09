#该程序处理同一变形量和压缩速率下不同温度的应力应变曲线
#预处理：删除应力应变前部分的正值和减序的应力应变数据（如没有则跳过），在将所有数值取绝对值，尾部数据选择处理
import pandas as pd
import sys
#文件路径和文件名
path = 'E:/4130x-GLEEBLE/data/70%/70%+1200℃/fix/'
filename = "1200.xlsx"
df = pd.read_excel(path+filename)

#列名index；自定义格式化
ColName = ["True Strain0.01","True Strain0.1","True Strain1","True Strain10"]
Col2Name = ["True Stress0.01","True Stress0.1","True Stress1","True Stress10"]
#数组接受数据
dataArr = []
fixedStrain = pd.DataFrame()

#将每组的应变部分实现左移至0开始，且与对应应力部分匹配装入dataframe类
for i in range(len(ColName)):
    temp = df[ColName[i]]-df[ColName[i]][0]
    dataArr.append(temp)
    fixedStrain = pd.concat([fixedStrain,dataArr[i],df[Col2Name[i]]],axis= 1)

#生成execl文件
fixedStrain.to_excel(path+'fixedStrainData.xlsx')
sys.exit()

