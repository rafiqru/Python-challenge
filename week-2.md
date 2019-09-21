# Python-challenge
## Data Management and Visualization
## Assignment-week-2 
Week 2:assignment
1) #load the libries
import pandas
import numpy
# read data ‘gapminderin python
data1=pandas.read_csv('my_nesarc.csv’, low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)#data type
data1.dtypes#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['CONSUMER’]=pandas.to_numeric(data1['CONSUMER’], errors='coerce’)# frequency count and percentage for nesarc data
print('count of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
f1=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f1)
print('Percentage of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
p1=data1['S2DQ1’].value_counts(normalize=True,sort=False, dropna=False)
print(p1)
print('count of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS’)
f2=data1['S2AQ2’].value_counts(sort=False, dropna=False)
print(f2)
print('percentage of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS’)
p2=data1['S2AQ2’].value_counts(normalize=True,sort=False, dropna=False)
print(p2)
print('COUNT of CONSUMER DRINKING STATUS’)
f3=data1['CONSUMER’].value_counts(sort=False, dropna=False)
print(f3)
print('percentage of CONSUMER DRINKING STATUS’)
p3=data1['CONSUMER’].value_counts(normalize=True,sort=False, dropna=False)
print(p3)
# subset of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
sub1=data1[(data1['S2AQ2’]==1)]
sub2=sub1.copy()
print(len(sub2))
# subset of DRINKING STATUS
sub3=data1[(data1['CONSUMER’]==1)]
sub4=sub3.copy()
print(len(sub4))#frequency
print('count for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf2=sub2['S2DQ1’].value_counts(sort=False)
print(gf2)
print('percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp2=sub2['S2DQ1’].value_counts(sort=False, normalize=True)
print(gp2)
print('Count for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf3=sub4['S2DQ1’].value_counts(sort=False)
print(gf3)
print('percentage for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp3=sub4['S2DQ1’].value_counts(sort=False, normalize=True)
print(gp3)

2)
Research question: Dependence of ALCOHOL CONSUMPTION on FAMILY HISTORY OF ALCOHOLISM
 FAMILY HISTORY (I) OF ALCOHOLISM
i.                    S2DQ1: BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
 1. Yes
2. No
9. Unknown
 ii. CONSUMER: DRINKING STATUS
 1. Current drinker
2. Ex-drinker
3. Lifetime Abstainer
 ii.                  ALCOHOL CONSUMPTION
S2AQ2: DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
 1. Yes
2. No
9. Unknown
 ## frequency table and percentage
count of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1     8124
2    32445
9     2524
Name: S2DQ1, dtype: int64
Percentage of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1   0.188522
2   0.752907
9   0.058571
Name: S2DQ1, dtype: float64
count of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
1    20836
2    22225
9       32
Name: S2AQ2, dtype: int64
percentage of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
1   0.483512
2   0.515745
9   0.000743
Name: S2AQ2, dtype: float64
COUNT of CONSUMER DRINKING STATUS
1    26946
2     7881
3     8266
Name: CONSUMER, dtype: int64
percentage of CONSUMER DRINKING STATUS
1   0.625299
2   0.182884
3   0.191818
Name: CONSUMER, dtype: float64
##Sub setting
count for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1     4357
2    15343
9     1136
Name: S2DQ1, dtype: int64
percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1   0.209109
2   0.736370
9   0.054521
Name: S2DQ1, dtype: float64
Count for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1     5544
2    19991
9     1411
Name: S2DQ1, dtype: int64
percentage for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER
1   0.205745
2   0.741891
9   0.052364
Name: S2DQ1, dtype: float64
 3)
Conclusion: It is observed that 48.4% have drank at least 12 alcoholic drinks in last 12 months and 62.5% are currently drinking. After sub setting,  It is found that about 20.9%% are drank at least 12 alcoholic drinks in last 12 months when they have family history of fathers’ are ever alcoholic or problem drinker. Besides, 20.6% are current drinkers when they have family history of fathers’ are ever alcoholic or problem drinker. From the both figures of alcohol status, it can be summarize that family history of alcoholism (when father ever an alcoholic or problem drinker) does not play a significant role to become alcoholism.
 ## Python code
#load the libries
import pandas
import numpy
# read data 'gapminderin python
data1=pandas.read_csv('my_nesarc.csv’, low_memory=False)
print(len(data1))
#all columns upper case
data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
#worked" convert to numeric as python read data as object(string)
data1['S2DQ1’]=pandas.to_numeric(data1['S2DQ1’], errors='coerce’)
data1['S2AQ3’]=pandas.to_numeric(data1['S2AQ3’], errors='coerce’)
data1['CONSUMER’]=pandas.to_numeric(data1['CONSUMER’], errors='coerce’)
# frequency count and percentage for nesarc data
print('count of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
f1=data1['S2DQ1’].value_counts(sort=False, dropna=False)
print(f1)
print('Percentage of BLOOD/NATURAL FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
p1=data1['S2DQ1’].value_counts(normalize=True,sort=False, dropna=False)
print(p1)
print('count of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS’)
f2=data1['S2AQ2’].value_counts(sort=False, dropna=False)
print(f2)
print('percentage of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS’)
p2=data1['S2AQ2’].value_counts(normalize=True,sort=False, dropna=False)
print(p2)
print('COUNT of CONSUMER DRINKING STATUS’)
f3=data1['CONSUMER’].value_counts(sort=False, dropna=False)
print(f3)
print('percentage of CONSUMER DRINKING STATUS’)
p3=data1['CONSUMER’].value_counts(normalize=True,sort=False, dropna=False)
print(p3)
# subset of DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS
sub1=data1[(data1['S2AQ2’]==1)]
sub2=sub1.copy()
print(len(sub2))
# subset of DRINKING STATUS
sub3=data1[(data1['CONSUMER’]==1)]
sub4=sub3.copy()
print(len(sub4))
#frequency
print('count for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf2=sub2['S2DQ1’].value_counts(sort=False)
print(gf2)
print('percentage for DRANK AT LEAST 12 ALCOHOLIC DRINKS IN LAST 12 MONTHS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp2=sub2['S2DQ1’].value_counts(sort=False, normalize=True)
print(gp2)
print('Count for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gf3=sub4['S2DQ1’].value_counts(sort=False)
print(gf3)
print('percentage for CONSUMER DRINKING STATUS given that FATHER EVER AN ALCOHOLIC OR PROBLEM DRINKER’)
gp3=sub4['S2DQ1’].value_counts(sort=False, normalize=True)
print(gp3)

