# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:28:17 2019

@author: mrafiq
"""
#w4 assignment data=gapminder
# research question: whether life ecpectancy depends on urban rate of population
#Week 4 assignment (graphical representation)
#load the libries
import pandas
import numpy
import seaborn
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('data_gapminder.csv', low_memory=False)
print(len(data1))
#all columns upper case
#data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#set pandas to to show all columns
pandas.set_option('display.max_columns', None)
#set pandas to to show all rows
pandas.set_option('display.max_rows', None)
# response is lifeexpectancy and explanatory variablevariable is urbanrate
#worked" convert to numeric as python read data as object(string)
data1['lifeexpectancy']=pandas.to_numeric(data1['lifeexpectancy'], errors='coerce')
data1['urbanrate']=pandas.to_numeric(data1['urbanrate'], errors='coerce')
#drop nan and make sub set
sub1=data1.dropna(subset=['lifeexpectancy','urbanrate'])
sub2=sub1.copy()
print(len(sub2))
# calculation of centre and spread
summary1=sub2['lifeexpectancy'].describe()
print(summary1)
summary2=sub2['urbanrate'].describe()
print(summary2)
##conver numerical to categorical
##make response and explanatory into categorical
sub2['c_lifeexpectancy']=pandas.cut(data1.lifeexpectancy,[0,60,100])
sub2['c_urbanrate']=pandas.cut(data1.urbanrate,[0,20,50,80,100])
#frequency
gf1=sub2.groupby('c_lifeexpectancy').size()
print(gf1)
gp1=sub2.groupby('c_lifeexpectancy').size()*100/len(sub2)
print(gp1)
gf2=sub2.groupby('c_urbanrate').size()
print(gf2)
gp2=sub2.groupby('c_urbanrate').size()*100/len(sub2)
print(gp2)
#conver numerical to categorical variable for graph
sub2['c_lifeexpectancy']=sub2['c_lifeexpectancy'].astype('category')
sub2['c_urbanrate']=sub2['c_urbanrate'].astype('category')
sub2.dtypes
#univariate grap for response (y)
seaborn.countplot(x='c_lifeexpectancy',data=sub2);
plt.xlabel(' life expectancy at birth ')
plt.ylabel('Number of countroes')
plt.title(' Countries of  life expectancy at birth')
#univariate grap for explanatory(x)
seaborn.countplot(x='c_urbanrate',data=sub2);
plt.xlabel('urban population (% of total')
plt.ylabel('Number of countroes')
plt.title(' Countries of urban population (% of total')
##for bivariate graph response should have to category 0 and 1 as follows
sub2['cc_lifeexpectancy']=sub2.c_lifeexpectancy.astype('category').cat.codes
gf3=sub2.groupby('cc_lifeexpectancy').size()
print(gf3)

# for bivariate graph need to convert response to numerical
sub2['cc_lifeexpectancy']=pandas.to_numeric(sub2['cc_lifeexpectancy'], errors='coerce')
# relation between response S2DQ1 and explanatory S2AQ3:bivariate bar graph
seaborn.factorplot(x='c_urbanrate',y='cc_lifeexpectancy',data=sub2, kind='bar', ci=None);
plt.xlabel('urban population (% of total')
plt.ylabel('Proportion of life expectancy at birth> 60')
plt.title('Proportion of life expectancy at birth (more than 60) for urban rate of total population')
## summary: it is noted that as the rate of urban population increases the life expectancy more than 60 years also increases. 
## it is evident that life expectancy depends on rate of urban population.
##it is interested to observe that the countries those urban rate is 80 to 100%, almost 100% of them live more than 60 years

