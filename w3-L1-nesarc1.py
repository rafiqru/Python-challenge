# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:41:31 2019

@author: mrafiq
"""

#lesson 3
# raltion between smoking and nicotine dependency
import pandas
import numpy
# read data in python
data1=pandas.read_csv('my_nesarc.csv', low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)
#bug fix for format to avoid run time error
pandas.set_option('display.float_format', lambda x:'%f'%x)

#data type
data1.dtypes

#worked conver data to numeric
data1['TAB12MDX']=pandas.to_numeric(data1['TAB12MDX'], errors='coerce')
data1['CHECK321']=pandas.to_numeric(data1['CHECK321'], errors='coerce')
data1['S3AQ3B1']=pandas.to_numeric(data1['S3AQ3B1'], errors='coerce')
data1['S3AQ3C1']=pandas.to_numeric(data1['S3AQ3C1'], errors='coerce')

# subset of young adult smoked last 12 month

sub1=data1[(data1['AGE']>=18) & (data1['AGE']<=25) & (data1['CHECK321']==1)]
sub2=sub1.copy()
#frequency
print('count for original S3AQ3B1')
c1=sub2['S3AQ3B1'].value_counts(sort=False)
print(c1)
#repacing missing values(9) by nan in python
sub2['S3AQ3B1']=sub2['S3AQ3B1'].replace(9, numpy.nan)
print('count for original S3AQ3B1 with 9 replace nan')
c2=sub2['S3AQ3B1'].value_counts(sort=False, dropna=False)
print(c2)
print('count for original S3AQ3C1')
c3=sub2['S3AQ3C1'].value_counts(sort=False,dropna=False)
print(c3)
sub2['S3AQ3C1']=sub2['S3AQ3C1'].replace(99, numpy.nan)
c4=sub2['S3AQ3C1'].value_counts(sort=False, dropna=False)
print(c4)
