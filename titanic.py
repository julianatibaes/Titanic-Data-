# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:31:51 2019

@author: Juliana Tibães

What factors made people more likely to survive?
- Gender
- Social Class
- Passager fare
- Women of social class 1 and 2 were more likely to survive.

gender? - yep
age? - nop
number of kids? - nop
cabin? - a lot of gaps

"""

import pandas as pd

path_data = 'C:\\Users\\36838.POSITIVO\\Documents\\Python Scripts\\udacity\\titanic\\titanic_data.csv'


# Mount dataframe
arch = pd.read_csv(path_data, sep = ',')
df = pd.DataFrame(arch)

df.head()

# see qtd nan values
df.isnull().sum()

# remove cabin column
df = df.drop('Cabin', axis=1)

# clean dataset
df.dropna(inplace=True)

#how many female and male
f = df['Sex'].loc[df['Sex'] == 'female'].count()
m = df['Sex'].loc[df['Sex'] == 'male'].count()

print("woman - ", f, "; man - ", m)
#woman -  259 ; man -  453

#how many female and male survived
f = df['Sex'].loc[df['Sex'] == 'female'].loc[df['Survived'] == 1].count()
m = df['Sex'].loc[df['Sex'] == 'male'].loc[df['Survived'] == 1].count()

print("woman - ", f, "; man - ", m)
#woman -  195 ; man -  93

df = df.apply(lambda x: x.replace('female', 0))
df = df.apply(lambda x: x.replace('male', 1))

df = df.apply(lambda x: x.replace('S', 0))
df = df.apply(lambda x: x.replace('C', 1))
df = df.apply(lambda x: x.replace('Q', 2))

df.corr()

df['Survived'].corr(df['Pclass']) # low
#-0.3564615884452385
df['Survived'].corr(df['Sex']) # moderate
#-0.5367616233485035
df['Survived'].corr(df['Fare'])  # low
#0.26609960047658043
df_f = df[df['Sex'] == 0]
df_m = df[df['Sex'] == 1]

df_f['Survived'].corr(df_f['Fare'])  # low
#0.22916713308902434
df_f['Survived'].corr(df_f['Pclass']) # moderate
#-0.5029284094167192
df_m['Survived'].corr(df_m['Pclass']) #low
#-0.2218932169299327

df_f['Pclass'].loc[df_f['Pclass'] == 1].loc[df_f['Survived'] == 1].count()
#Out[45]: 80
df_f['Pclass'].loc[df_f['Pclass'] == 2].loc[df_f['Survived'] == 1].count()
#Out[46]: 68
df_f['Pclass'].loc[df_f['Pclass'] == 3].loc[df_f['Survived'] == 1].count()
#Out[47]: 47

df_f['Survived'].corr(df_f['Pclass']==1)
# Out[48]: 0.3358726328341041
df_f['Survived'].corr(df_f['Pclass']==2)
# Out[49]: 0.24343956234108827
df_f['Survived'].corr(df_f['Pclass']==3)
#Out[50]: -0.5458725999872418



