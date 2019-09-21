# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
print(pandas.__version__)
import numpy
data1=pandas.read_csv('data_gapminder.csv')
data1=pandas.read_csv('data_gapminder.csv', low_memory=False)
#data type
data1.dtypes
print(len(data1))
print(len(data1.columns))
#make the variable numeric
data1['lifeexpectancy'].apply(convert_currency)
data1['lifeexpectancy']=data1['lifeexpectancy'].replace(',','').type(float)
data1['lifeexpectancy']=data1['lifeexpectancy'].convert_objects(convert_numeric=True)
data1['urbanrate']=data1['urbanrate'].convert_objects(convert_numeric=True)


#find frequency
print('count of life expectancy at birth (years)')
f1=data1['lifeexpectancy'].value_counts(sort=False,dropna=False)
print(f1)
#find percentage
print('percentage of life expectancy at birth (years)')
p1=data1['lifeexpectancy'].value_counts(sort=False, normalize=True)
print(p1)
print('count of urban population (% of total)')
f2=data1['urbanrate'].value_counts(sort=False)
print(f2)
print('percentage of urban population (% of total)')
p2=data1['urbanrate'].value_counts(sort=False, normalize=True)
print(p2)