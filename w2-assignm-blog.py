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
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
data1['S2AQ3']=pandas.to_numeric(data1['S2AQ3'], errors='coerce')
data1['CONSUMER']=pandas.to_numeric(data1['CONSUMER'], errors='coerce')

# frequency count and percentage for nesarc data
print('count of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
f1=data1['S2DQ1'].value_counts(sort=False, dropna=False)
print(f1)
print('Percentage of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
p1=data1['S2DQ1'].value_counts(normalize=True,sort=False, dropna=False)
print(p1)
print('count of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS')
f2=data1['S2AQ2'].value_counts(sort=False, dropna=False)
print(f2)
print('percentage of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS')
p2=data1['S2AQ2'].value_counts(normalize=True,sort=False, dropna=False)
print(p2)
print('COUNT of CONSUMER DRINKING STATUS')
f3=data1['CONSUMER'].value_counts(sort=False, dropna=False)
print(f3)
print('percentage of CONSUMER DRINKING STATUS')
p3=data1['CONSUMER'].value_counts(normalize=True,sort=False, dropna=False)
print(p3)
# subset of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
sub1=data1[(data1['S2AQ2']==1)]
sub2=sub1.copy()
print(len(sub2))
# subset of DRINKING STATUS
sub3=data1[(data1['CONSUMER']==1)]
sub4=sub3.copy()
print(len(sub4))

#frequency
print('count for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gf2=sub2['S2DQ1'].value_counts(sort=False)
print(gf2)
print('percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gp2=sub2['S2DQ1'].value_counts(sort=False, normalize=True)
print(gp2)
print('Count for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gf3=sub4['S2DQ1'].value_counts(sort=False)
print(gf3)
print('percentage for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gp3=sub4['S2DQ1'].value_counts(sort=False, normalize=True)
print(gp3)

