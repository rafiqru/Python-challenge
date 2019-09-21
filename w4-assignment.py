# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:20:03 2019

@author: DELL PC
"""
#Week 4 assignment (graphical representation)
#load the libries
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('my_nesarc.csv', low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#set pandas to to show all columns
pandas.set_option('display.max_columns', None)
#set pandas to to show all rows
pandas.set_option('display.max_rows', None)
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
data1['S2AQ3']=pandas.to_numeric(data1['S2AQ3'], errors='coerce')
data1['S2AQ6B']=pandas.to_numeric(data1['S2AQ8A'], errors='coerce')
data1['CONSUMER']=pandas.to_numeric(data1['CONSUMER'], errors='coerce')
#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1')
f1=data1['S2DQ1'].value_counts(sort=False,dropna=False)
print(f1)
print('count for S2DQ1 by replacing missing with nan')
data1['S2DQ1']=data1['S2DQ1'].replace(9, numpy.nan)
f11=data1['S2DQ1'].value_counts(sort=False, dropna=False)
print(f11)
print('count for orginal S2AQ3')
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
print(f33)  
print('count for original CONSUMER')
f4=data1['CONSUMER'].value_counts(sort=False,dropna=False)
print(f4)


# ALSO INCLUDE BL.: NA, did not drink or unknown if drank wine in last 12 months
# who said they did not drink AT LEAST 1 ALCOHOLIC DRINK IN LAST 12 MONTHS(S2AQ3), they no need TO ASK HOW OFTEN THEY DRINK WINE IN THE
#LAST 12 MONTH IN S2AQ6B AND CAN BE SOLVED AS FOLLOWS  by including who did not drinl last 12 months from the unknown
data1.loc[(data1['S2AQ3']!=9) & (data1['S2AQ6B'].isnull()),'S2AQ6B']=11
#recode-recoding S2AQ6B where higher value means drink more frequently names as NEWS2AQ6B
recode1={1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
data1['NEWS2AQ6B']=data1['S2AQ6B'].map(recode1)
print('count for RECORDED NEWS2AQ6B')
f5=data1['NEWS2AQ6B'].value_counts(sort=False,dropna=False)
print(f5)
# select rows: subset of data1 according to YEAR OF SCHOOL COMPLETED(S1Q6A) is high school or some college
sub1=data1[(data1.S1Q6A== 8) | (data1.S1Q6A == 10)]
sub2=sub1.copy()
print(len(sub2))
#conver numerical to categorical variable for graph
sub2['S2DQ1']=sub2['S2DQ1'].astype('category')
sub2['S2AQ3']=sub2['S2AQ3'].astype('category')
sub2['NEWS2AQ6B']=sub2['NEWS2AQ6B'].astype('category')
sub2['CONSUMER']=sub2['CONSUMER'].astype('category')
#grpahs
seaborn.countplot(x='S2DQ1',data=sub2);
plt.xlabel('FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER')
plt.title('FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER given that COMPLETED high school or some college')
seaborn.countplot(x='S2AQ3',data=sub2)
plt.xlabel('DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS')
plt.title('DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that COMPLETED high school or some college')
seaborn.countplot(x='NEWS2AQ6B',data=sub2);
plt.xlabel('HOW OFTEN DRANK WINE IN LAST 12 MONTHS')
plt.title('HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that COMPLETED high school or some college')
seaborn.countplot(x='CONSUMER',data=sub2);
plt.xlabel('DRINKING STATUS')
plt.title('DRINKING STATUS given that COMPLETED high school or some college')

#frequency OF SUBSET
gf1=sub2.groupby('S2DQ1').size()
print(gf1)
gp1=sub2.groupby('S2DQ1').size()*100/len(data1)
print(gp1)
gf2=sub2.groupby('S2AQ3').size()
print(gf2)
gp2=sub2.groupby('S2AQ3').size()*100/len(data1)
print(gp2)
gf3=sub2.groupby('NEWS2AQ6B').size()
print(gf3)
gp3=sub2.groupby('NEWS2AQ6B').size()*100/len(data1)
print(gp3)
gf4=sub2.groupby('CONSUMER').size()
print(gf4)
gp4=sub2.groupby('CONSUMER').size()*100/len(data1)
print(gp4)

#for bivariate graph response should have to category 0 and 1. so do this by reoplace a new varoable BS2DQ1
#replace 0 to no and 1 to yes
sub2['BS2DQ1']=sub2['S2DQ1'].replace([1,2],[1,0])
sub2['BS2DQ1']=pandas.to_numeric(data1['BS2DQ1'], errors='coerce')

gf5=sub2.groupby('BS2DQ1').size()
print(gf5)
# for bivariate graph need to convert response to numerical
data1['S2DQ1']=pandas.to_numeric(data1['S2DQ1'], errors='coerce')
# relation between response S2DQ1 and explanatory S2AQ3:bivariate bar graph
seaborn.factorplot(x='CONSUMER',y='BS2DQ1',data=sub2, kind='bar', ci=None);
plt.xlabel('DRINKING STATUS')
plt.ylabel('Proportion of FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER ')

#for Examine both their center and spread, we used gapminder data
data2=pandas.read_csv('data_gapminder.csv',  low_memory=False)
summary1=data2['ifeexpectancy'].describe()
print(summary1)