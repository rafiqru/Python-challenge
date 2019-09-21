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
# read data 'nesarc in python
data1=pandas.read_csv('my_nesarc.csv', low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)

#data type
data1.dtypes

#worked" convert to numeric as python read data as object(string)
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
data1['S2AQ3']=pandas.to_numeric(data1['S2AQ3'], errors='coerce')
data1['S2AQ6B']=pandas.to_numeric(data1['S2AQ8A'], errors='coerce')

#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1')
f1=data1['S2DQ1'].value_counts(sort=False,dropna=False)
print(f1)
print('count for S2DQ1 by replacing missing with nan')
data1['S2DQ1']=data1['S2DQ1'].replace(9, numpy.nan)
f11=data1['S2DQ1'].value_counts(sort=False, dropna=False)
print(f11)
print('count for original S2AQ3')
f2=data1['S2AQ3'].value_counts(sort=False,dropna=False)
print(f2)
print('count for S2AQ3 by replacing missing with nan')
data1['S2AQ3']=data1['S2AQ3'].replace(9,numpy.nan)
f22=data1['S2AQ3'].value_counts(sort=False, dropna=False)
print(f22)
print('count for original S2AQ6B')
f3=data1['S2AQ6B'].value_counts(sort=False,dropna=False)
print(f3)
print('count for S2AQ6B by replacing missing with nan')
data1['S2AQ6B']=data1['S2AQ6B'].replace(99,numpy.nan)
f33=data1['S2AQ6B'].value_counts(sort=False, dropna=False)
print(f33)  # ALSO INCLUDE BL.: NA, did not drink or unknown if drank wine in last 12 months
# who said they did not drink AT LEAST 1 ALCOHOLIC DRINK IN LAST 12 MONTHS(S2AQ3), they no need TO ASK HOW OFTEN THEY DRINK WINE IN THE 
#LAST 12 MONTH IN S2AQ6B AND CAN BE SOLVED AS FOLLOWS  by including who did not drinl last 12 months from the unknown
data1.loc[(data1['S2AQ3']!=9) & (data1['S2AQ6B'].isnull()),'S2AQ6B']=11
#recode-recoding S2AQ6B where higher value means drink more frequently names as NEWS2AQ6B
recode1={1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
data1['NEWS2AQ6B']=data1['S2AQ6B'].map(recode1)
print('count for RECORDED NEWS2AQ6B')
f4=data1['NEWS2AQ6B'].value_counts(sort=False,dropna=False)
print(f4)
# select rows: subset of data1 given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER'
sub1=data1[(data1['S2DQ1']==1)]
sub2=sub1.copy()
print(len(sub2))

#frequency OF SUBSET
print('count for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gf2=sub2['S2AQ3'].value_counts(sort=False, dropna=False)
print(gf2)
print('percentage for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gp2=sub2['S2AQ3'].value_counts(sort=False, normalize=True,dropna=False)
print(gp2)
print('Count for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gf3=sub2['NEWS2AQ6B'].value_counts(sort=False, dropna=False)
print(gf3)
print('percentage for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
gp3=sub2['NEWS2AQ6B'].value_counts(sort=False, normalize=True, dropna=False)
print(gp3)

