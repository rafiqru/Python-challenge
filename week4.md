# Python-challenge
## 1-Data Management and Visualization
## Week 4 assignment (graphical representation) import pandas
# research question: whether life expectancy depends on urban rate of population?
import numpy
import seaborn
import matplotlib.pyplot as plt
# read data 'nesarc in python
data1=pandas.read_csv('data_gapminder.csv', low_memory=False)
print(len(data1))
213
#all columns upper case
#data1.columns=map(str.upper,data1.columns)
#data type
data1.dtypes
Out[11]: 
country                 object
incomeperperson         object
alcconsumption          object
armedforcesrate         object
breastcancerper100th    object
co2emissions            object
femaleemployrate        object
hivrate                 object
internetuserate         object
lifeexpectancy          object
oilperperson            object
polityscore             object
relectricperperson      object
suicideper100th         object
employrate              object
urbanrate               object
dtype: object
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
188
# calculation of centre and spread
summary1=sub2['lifeexpectancy'].describe()
print(summary1)
count    188.000000
mean      69.600702
std        9.708289
min       47.794000
25%       63.952250
50%       73.126500
75%       76.236750
max       83.394000
Name: lifeexpectancy, dtype: float64
summary2=sub2['urbanrate'].describe()

print(summary2)
count    188.000000
mean      55.932766
std       23.286464
min       10.400000
25%       36.745000
50%       57.230000
75%       73.465000
max      100.000000
Name: urbanrate, dtype: float64
##conver numerical to categorical
##make response and explanatory into categorical
sub2['c_lifeexpectancy']=pandas.cut(data1.lifeexpectancy,[0,60,100])
sub2['c_urbanrate']=pandas.cut(data1.urbanrate,[0,20,50,80,100])
#frequency
gf1=sub2.groupby('c_lifeexpectancy').size()
print(gf1)
c_lifeexpectancy
(0, 60]       38
(60, 100]    150
dtype: int64
gp1=sub2.groupby('c_lifeexpectancy').size()*100/len(sub2)
print(gp1)
c_lifeexpectancy
(0, 60]      20.212766
(60, 100]    79.787234
dtype: float64
Conclusion: It is observed that almost 80% of the countries life expectancy is more than 60 years and only 20% of the countries life expectancy is up to 60 years.
gf2=sub2.groupby('c_urbanrate').size()

print(gf2)
c_urbanrate
(0, 20]      12
(20, 50]     64
(50, 80]     79
(80, 100]    33
dtype: int64
gp2=sub2.groupby('c_urbanrate').size()*100/len(sub2)
print(gp2)
c_urbanrate
(0, 20]       6.382979
(20, 50]     34.042553
(50, 80]     42.021277
(80, 100]    17.553191
dtype: float64
Conclusion: It is evident that 42% of countries urban rate of population is 51-80% and only 17.6%  of countries urban rate of population 81-100%, whereas  almost 40% of countries urban rate of population rate is up to 50%.
#convert numerical to categorical variable for graph
sub2['c_lifeexpectancy']=sub2['c_lifeexpectancy'].astype('category')
sub2['c_urbanrate']=sub2['c_urbanrate'].astype('category')
sub2.dtypes
Out[45]: 
country                   object
incomeperperson           object
alcconsumption            object
armedforcesrate           object
breastcancerper100th      object
co2emissions              object
femaleemployrate          object
hivrate                   object
internetuserate           object
lifeexpectancy           float64
oilperperson              object
polityscore               object
relectricperperson        object
suicideper100th           object
employrate                object
urbanrate                float64
c_lifeexpectancy        category
c_urbanrate             category
dtype: object
#univariate grap for response (y)
seaborn.countplot(x='c_lifeexpectancy',data=sub2);
plt.xlabel(' life expectancy at birth ')
plt.ylabel('Number of countroes')
plt.title(' Countries of  life expectancy at birth')
Out[47]: Text(0.5, 1.0, ' Countries of  life expectancy at birth')
 

Conclusion: It is observed that almost 80% of the (150)countries life expectancy is more than 60 years and only 20% of the (38) countries life expectancy is up to 60 years.

#univariate grap for explanatory(x)
seaborn.countplot(x='c_urbanrate',data=sub2);
plt.xlabel('urban population (% of total')
plt.ylabel('Number of countroes')
plt.title(' Countries of urban population (% of total')
Out[49]: Text(0.5, 1.0, ' Countries of urban population (% of total')
 
Conclusion: It is evident that 42% of (79) countries urban rate of population is 51-80% and only 17.6%  of countries (33) urban rate of population 81-100%, whereas  almost 40% of countries (76) urban rate of population rate is up to 50%.


##for bivariate graph response should have to category 0 and 1 as follows
sub2['cc_lifeexpectancy']=sub2.c_lifeexpectancy.astype('category').cat.codes
gf3=sub2.groupby('cc_lifeexpectancy').size()
print(gf3)
cc_lifeexpectancy
0     38
1    150
dtype: int64
# for bivariate graph need to convert response to numerical
sub2['cc_lifeexpectancy']=pandas.to_numeric(sub2['cc_lifeexpectancy'], errors='coerce')
#relation between response S2DQ1 and explanatory S2AQ3:bivariate bar graph
seaborn.factorplot(x='c_urbanrate',y='cc_lifeexpectancy',data=sub2, kind='bar', ci=None);
plt.xlabel('urban population (% of total')
plt.ylabel('Proportion of life expectancy at birth> 60')
plt.title('Proportion of life expectancy at birth (more than 60) for urban rate of total population')
C:\Users\mrafiq\AppData\Local\Continuum\anaconda3\lib\site-packages\seaborn\categorical.py:3666: UserWarning: The `factorplot` function has been renamed to `catplot`. The original name will be removed in a future release. Please update your code. Note that the default `kind` in `factorplot` (`'point'`) has changed `'strip'` in `catplot`.
  warnings.warn(msg)
Out[57]: Text(0.5, 1, 'Proportion of life expectancy at birth (more than 60) for urban rate of total population')
 

## Summary: it is noted that as the rate of urban population increases the life expectancy more than 60 years also increases. 
## it is evident that life expectancy depends on rate of urban population.
##it is also interested to observe that the countries those urban rate is 80 to 100%, almost 100% of them live more than 60 years
