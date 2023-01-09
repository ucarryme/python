from contextlib import nullcontext
from datetime import date
from fileinput import filename
from os import TMP_MAX
import pandas as pd
path = 'E:/4130x-GLEEBLE/data/0.01/0.01+70%/fix/'
filename = "0.01+70%+T.xlsx"
df = pd.read_excel(path+filename)

ColName = ["True Strain900","True Strain950","True Strain1000","True Strain1050","True Strain1100","True Strain1200"]
RowName = ["True Stress900","True Stress950","True Stress1000","True Stress1050","True Stress1100","True Stress1200"]
dataFrame = []
fixedStrain = pd.DataFrame()
for i in range(6):
    temp = df[ColName[i]]-df[ColName[i]][0]
    dataFrame.append(temp)
    fixedStrain = pd.concat([fixedStrain,dataFrame[i],df[RowName[i]]],axis= 1)
print(type(dataFrame[0]))
"""
dateFrame_0 = df[ColName[0]]-df[ColName[0]][0]
dateFrame_1 = df[ColName[1]]-df[ColName[1]][0]
dateFrame_2 = df[ColName[2]]-df[ColName[2]][0]
dateFrame_3 = df[ColName[3]]-df[ColName[3]][0]
dateFrame_4 = df[ColName[4]]-df[ColName[4]][0]
dateFrame_5 = df[ColName[5]]-df[ColName[5]][0]
fixedStrain = pd.concat([dateFrame_0,dateFrame_1,dateFrame_2,dateFrame_3,dateFrame_4,dateFrame_5],axis= 1)
"""

#fixedStrain = pd.concat([dataFrame[0],dataFrame[1],dataFrame[2],dataFrame[3],dataFrame[4],dataFrame[5]],axis= 1)

fixedStrain.to_excel(path+'fixedStrainData.xlsx')

