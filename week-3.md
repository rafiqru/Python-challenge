# Python-challenge
## Data Management and Visualization
## week3-assignment
W 3: assignment: Making Data Management Decisions
import pandas
import numpy
data1=pandas.read_csv(‘my_nesarc.csv’, low_memory=False)
data1.columns=map(str.upper,data1.columns)
data1.dtypes
Out[91]:
UNNAMED: 0        int64
ETHRACE2A         int64
ETOTLCA2         object
IDNUM             int64
PSU               int64
HER12ABDEP        int64
HERP12ABDEP       int64
OTHB12ABDEP       int64
OTHBP12ABDEP      int64
NDSYMPTOMS      float64
Length: 3010, dtype: object
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['S2AQ6B’]=pandas.to_numeric(data1['S2AQ8A’], errors='coerce’)
#replacing missing values for nan
print('count for original S2DQ1’)
count for original S2DQ1
f1=data1['S2DQ1’].value_counts(sort=False)
print(f1)
1     8124
2    32445
9     2524
Name: S2DQ1, dtype: int64
print('count for S2DQ1 by replacing missing with nan’)
count for S2DQ1 by replacing missing with nan
data1['S2DQ1’]=data1['S2DQ1’].replace(9, numpy.nan)
f11=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f11)
1.0     8124
2.0    32445
NaN     2524
Name: S2DQ1, dtype: int64
print('count for original S2AQ3’)
count for original S2AQ3
f2=data1['S2AQ3’].value_counts(sort=False)
print(f2)
1    26946
2    16116
9       31
Name: S2AQ3, dtype: int64
print('count for S2AQ3 by replacing missing with nan’)
count for S2AQ3 by replacing missing with nan
data1['S2AQ3’]=data1['S2AQ3’].replace(9,numpy.nan)
f22=data1['S2AQ3’].value_counts(sort=False, dropna=False)
print(f22)
2.0    16116
1.0    26946
NaN       31
Name: S2AQ3, dtype: int64
print('count for original S2AQ6B’)
count for original S2AQ6B
f3=data1['S2AQ6B’].value_counts(sort=False)
print(f3)
10.0    3637
8.0     1805
3.0     2619
4.0     2914
2.0     1210
1.0     1865
9.0     3210
5.0     3261
99.0     205
6.0     3557
7.0     2663
Name: S2AQ6B, dtype: int64
f3=data1['S2AQ6B’].value_counts(sort=False,dropna=False)
print(f3)
NaN     16147
8.0      1805
3.0      2619
4.0      2914
2.0      1210
1.0      1865
9.0      3210
10.0     3637
99.0      205
6.0      3557
5.0      3261
7.0      2663
Name: S2AQ6B, dtype: int64
print('count for S2AQ6B by replacing missing with nan’)
count for S2AQ6B by replacing missing with nan
data1['S2AQ6B’]=data1['S2AQ6B’].replace(99,numpy.nan)
f33=data1['S2AQ6B’].value_counts(sort=False, dropna=False)
print(f33)  # ALSO INCLUDE BL.: NA, did not drink or unknown if drank wine in last 12 months
NaN     16352
8.0      1805
3.0      2619
4.0      2914
2.0      1210
1.0      1865
9.0      3210
10.0     3637
6.0      3557
5.0      3261
7.0      2663
Name: S2AQ6B, dtype: int64
#recode-recoding S2AQ6B where higher value means drink more frequently names as NEWS2AQ6B
recode1={1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
data1['NEWS2AQ6B’]=data1['S2AQ6B’].map(recode1)
print('count for RECORDED NEWS2AQ6B’)
count for RECORDED NEWS2AQ6B
f4=data1['NEWS2AQ6B’].value_counts(sort=False,dropna=False)
print(f4)
NaN     16352
1.0      3637
6.0      3261
8.0      2619
4.0      2663
2.0      3210
9.0      1210
5.0      3557
3.0      1805
10.0     1865
7.0      2914
Name: NEWS2AQ6B, dtype: int64
sub1=data1[(data1['S2DQ1’]==1)]
print(len(sub2))8124
print('count for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
count for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
gf2=sub2['S2AQ3’].value_counts(sort=False, dropna=False)
print(gf2)
2.0    2579
1.0    5544
NaN       1
Name: S2AQ3, dtype: int64
print('percentage for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
percentage for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
gp2=sub2['S2AQ3’].value_counts(sort=False, normalize=True,dropna=False)
2.0    0.317454
1.0    0.682422
NaN    0.000123
Name: S2AQ3, dtype: float64
print(gp2)
print('Count for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
Count for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
gf3=sub2['NEWS2AQ6B’].value_counts(sort=False, dropna=False)
print(gf3)
NaN     2601
1.0      709
9.0      256
8.0      581
7.0      567
5.0      790
4.0      515
6.0      631
2.0      693
3.0      382
10.0     399
Name: NEWS2AQ6B, dtype: int64
print('percentage for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
percentage for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
gp3=sub2['NEWS2AQ6B’].value_counts(sort=False, normalize=True, dropna=False)
print(gp3)
NaN     0.320162
1.0     0.087272
9.0     0.031512
8.0     0.071516
7.0     0.069793
5.0     0.097243
4.0     0.063392
6.0     0.077671
2.0     0.085303
3.0     0.047021
10.0    0.049114
Name: NEWS2AQ6B, dtype: float64
CONCLUSION: it is interested to note that 68.2% OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER. 
Pythin program
#load the libries
import pandas
import numpy
# read data 'nesarc in python
data1=pandas.read_csv('my_nesarc.csv’, low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['S2AQ6B’]=pandas.to_numeric(data1['S2AQ8A’], errors='coerce’)
#replacing missing values for nan (ALSO 9 OR 99 CONSIDERING MISSING)
print('count for original S2DQ1’)
f1=data1['S2DQ1’].value_counts(sort=False,dropna=False)
print(f1)
print('count for S2DQ1 by replacing missing with nan’)
data1['S2DQ1’]=data1['S2DQ1’].replace(9, numpy.nan)
f11=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f11)
print('count for original S2AQ3’)
f2=data1['S2AQ3’].value_counts(sort=False,dropna=False)
print(f2)
print('count for S2AQ3 by replacing missing with nan’)
data1['S2AQ3’]=data1['S2AQ3’].replace(9,numpy.nan)
f22=data1['S2AQ3’].value_counts(sort=False, dropna=False)
print(f22)
print('count for original S2AQ6B’)
f3=data1['S2AQ6B’].value_counts(sort=False,dropna=False)
print(f3)
print('count for S2AQ6B by replacing missing with nan’)
data1['S2AQ6B’]=data1['S2AQ6B’].replace(99,numpy.nan)
f33=data1['S2AQ6B’].value_counts(sort=False, dropna=False)
print(f33)  # ALSO INCLUDE BL.: NA, did not drink or unknown if drank wine in last 12 months
# who said they did not drink AT LEAST 1 ALCOHOLIC DRINK IN LAST 12 MONTHS(S2AQ3), they no need TO ASK HOW OFTEN THEY DRINK WINE IN THE
#LAST 12 MONTH IN S2AQ6B AND CAN BE SOLVED AS FOLLOWS  by including who did not drinl last 12 months from the unknown
data1.loc[(data1['S2AQ3’]!=9) & (data1['S2AQ6B’].isnull()),'S2AQ6B’]=11
#recode-recoding S2AQ6B where higher value means drink more frequently names as NEWS2AQ6B
recode1={1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
data1['NEWS2AQ6B’]=data1['S2AQ6B’].map(recode1)
print('count for RECORDED NEWS2AQ6B’)
f4=data1['NEWS2AQ6B’].value_counts(sort=False,dropna=False)
print(f4)
# select rows: subset of data1 given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’
sub1=data1[(data1['S2DQ1’]==1)]
sub2=sub1.copy()
print(len(sub2))
#frequency OF SUBSET
print('count for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf2=sub2['S2AQ3’].value_counts(sort=False, dropna=False)
print(gf2)
print('percentage for DRANK AT LEAST 1 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp2=sub2['S2AQ3’].value_counts(sort=False, normalize=True,dropna=False)
print(gp2)
print('Count for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf3=sub2['NEWS2AQ6B’].value_counts(sort=False, dropna=False)
print(gf3)
print('percentage for HOW OFTEN DRANK WINE IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp3=sub2['NEWS2AQ6B’].value_counts(sort=False, normalize=True, dropna=False)
print(gp3)

