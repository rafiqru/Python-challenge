# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:41:31 2019

@author: mrafiq
"""
# Research question: dependence of ALCOHOL CONSUMPTION on FAMILY HISTORY  OF ALCOHOLISM
#w2-assignment
#load the libries
import pandas
import numpy
# read data 'gapminderin python
data1=pandas.read_csv('my_nesarc.csv', low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)

#data type
data1.dtypes

#worked" convert to numeric as python read data as object(string)
#data1['S2DQ1']=data1['S2DQ1'].convert_objects(convert_numeric=True) # AttributeError
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
data1['S2AQ1']=pandas.to_numeric(data1['S2AQ1'], errors='coerce')
data1['S2AQ2']=pandas.to_numeric(data1['S2AQ2'], errors='coerce')
data1['S2AQ3']=pandas.to_numeric(data1['S2AQ3'], errors='coerce')
data1['CONSUMER']=pandas.to_numeric(data1['CONSUMER'], errors='coerce')

# frequency count and percentage for nesarc data
print('count of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
f1=data1['S2DQ1'].value_counts(sort=False, dropna=False)
print(f1)
print('percentage of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
p1=data1['S2DQ1'].value_counts(sort=False,dropna=False, normalize=True)
print(p1)
print('count  of DRANK AT LEAST 1 ALCOHOLIC DRINK IN LIFE')
f2=data1['S2AQ1'].value_counts(sort=False, dropna=False)
print(f2)
print('percentage of DRANK AT LEAST 1 ALCOHOLIC DRINK IN LIFE')
p2=data1['S2AQ1'].value_counts(normalize=True,sort=False, dropna=False)
print(p2)
print('count of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS')
f3=data1['S2AQ2'].value_counts(sort=False, dropna=False)
print(f3)
print('percentage of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS')
p3=data1['S2AQ2'].value_counts(normalize=True,sort=False, dropna=False)
print(p3)
print('count of DRANK AT LEAST 1 ALCOHOLIC DRINK IN LAST 12 MONTHS')
f4=data1['S2AQ3'].value_counts(sort=False, dropna=False)
print(f4)
print('percentage of DRANK AT LEAST 1 ALCOHOLIC DRINK IN LAST 12 MONTHS')
p4=data1['S2AQ3'].value_counts(normalize=True,sort=False, dropna=False)
print(p4)
print('COUNT of CONSUMER DRINKING STATUS')
f5=data1['CONSUMER'].value_counts(sort=False, dropna=False)
print(f4)
print('percentage of CONSUMER DRINKING STATUS')
p5=data1['CONSUMER'].value_counts(normalize=True,sort=False, dropna=False)
print(p5)
#By group
print('count  of NICOTINE DEPENDENCE by group') 
gf1=data1.groupby('S2DQ1').size()
print(gf1)
print('percentage of NICOTINE DEPENDENCE by group')
gp1=data1.groupby('TAB12MDX').size()*100/len(data1)
print(gp1)
print('count  of CIGARETTE SMOKING STATUS by group')
gf2=data1.groupby('CHECK321').size()
print(gf2)
print('percentage of CIGARETTE SMOKING STATUS by group')
gp2=data1.groupby('CHECK321').size()*100/len(data1)
print(gp2)
print('count  of USUAL FREQUENCY WHEN SMOKED CIGARETTES by group')
gf3=data1.groupby('S3AQ3B1').size()
print(gf3)
print('percentage of USUAL FREQUENCY WHEN SMOKED CIGARETTESby group')
gp3=data1.groupby('S3AQ3B1').size()*100/len(data1)
print(gp3)
print('count  of USUAL QUANTITY WHEN SMOKED CIGARETTES by group')
gf4=data1.groupby('S3AQ3C1').size()
print(gf4)
print('percentage of USUAL QUANTITY WHEN SMOKED CIGARETTES by group')
gp4=data1.groupby('S3AQ3C1').size()*100/len(data1)
print(gp4)
# subset of FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(yes=1)
sub1=data1[(data1['S2DQ1']==1)]
sub2=sub1.copy()
print(len(sub2))
# subset of  FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(no=2)
sub3=data1[(data1['S2DQ1']==2)]
sub4=sub3.copy()
print(len(sub4))

#frequency
print('count for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(yes=1)')
gf3=sub2['S2AQ2'].value_counts(sort=False)
print(gf3)
print('percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(yes=1)')
gp3=sub2['S2AQ2'].value_counts(sort=False, normalize=True)
print(gp3)
print('count DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(no=2)')
gf32=sub4['S2AQ2'].value_counts(sort=False)
print(gf32)
print('percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER(no=2)')
gp32=sub4['S2AQ2'].value_counts(sort=False, normalize=True)
print(gp32)
