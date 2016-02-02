# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:57:20 2016

@author: dyu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

test=pd.read_csv('Test.csv')

#exploratory code
test.head()
test.tail()
test.dtypes

test.columns
test.columns=[col.lower() for col in test]
test.rename(columns={'unnamed: 0':'num_id', 'months since last donation':'mo_last_donation', 'number of donations':'num_donations', 'total volume donated (c.c.)':'vol_donated', 'months since first donation':'mo_first_donation'}, inplace=True)

test.num_id.duplicated().sum()
#thereare 28 dupes
test[test.duplicated()]
#show duplicate rows 
test.drop_duplicates(inplace=True)
#check missing values
test.num_id.isnull().sum()


#correlation heatmap between variables
sns.set(style="white")
corr = test.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
           square=True,
           linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

#negative correlations between mo_last_donation and vol_donated, num_donations
#positive correlations betwen num_donations and mo_first_donation_vol_donated
#positive correlations between vol_donated and mo_first_donation

'''
Visualizations
'''
#scatterplot beween two variables that had no correlation
plt.scatter(test.num_donations, test.mo_last_donation)
plt.scatter(test.mo_first_donation, test.mo_last_donation)




col_names=['num_id', 'mo_last_donation', 'num_donations', 'vol_donated', 'mo_first_donation']

