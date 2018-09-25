# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 07:40:28 2018

@author: Jarod
"""

import pandas as pd
import numpy as np

#1.	Read in the data set.
df = pd.read_csv("flights.csv")

#2.	Display the first 50 data entries/rows as well as last 50 entries/rows.
h = df.head(50)
print("First 50 rows")
print(h)
print()
t = df.tail(50)
print("Last 50 rows")
print()
print(t)

#3.	Display a quick statistical information on all numerical columns such as count, mean, std, min, max, etc. 
description = df.describe()
print("Description")
print(description)
print()

#4.	Select a subset of rows (you decide which subset to select or which criteria to use for selection.) 
#Display the first 10 data entries selected.
print("Rows by Destination")
rDest = df.iloc[10:100]
print(rDest.head(10))
print()

#5.	Similar to 4, but select a subset of columns (from original data). 
#Display the first 10 data entries with selected columns.
fColumns = df['origin'].head(10)
print(fColumns)
print()

#6.	From original data, filter out some data, for example, filter out those salary lower than certain amount. 
#After filtering out the data, display the first 50 data entries. 
df_lax = df[df['dest'] == 'LAX']
print("Rows only with LAX as the destination")
print(df_lax['dest'].head(50))
print()

#7.	From original data, find out all entries with missing values. Display the first 10 entries.
f_M = df[df.isnull().any(axis=1)]
print("First 10 missing values")
print(f_M.head(10))
print()

#8.	Manipulate the original data by changing numerical values of specific column(s) (for example, give everyone 10% raise!) Display the first 10 entries before update and after update.
print("Previous air time")
prev = df['air_time']
print(prev.head(10))
print("Increasing the air time")
df['air_time']=10*df['air_time']
small = df.head(10)
print(small)
print()

#9.	Sort the data set resulted from step 8 in certain way (e.g.  descending order of salaries)
print("Ascending air times")
sAir = small.sort_values(by='air_time')
print(sAir)
print()

#10.	Group the data set from step 9 based on certain category (e.g. group based on rank of Professor, Assoc Professor, etc.)
print("Grouped by carrier")
rAir = sAir.sort_values(by='carrier')
print(rAir[['air_time','carrier']])
print()

#11.	Plot data (or subset of data) in at least three different ways such as vertical bar graph, horizontal bar graph, curve, … 
df.boxplot()
ax = df.plot(xticks = range(10), legend = True, style = ['r+-','gx-','b*-'], title = 'Flight Chart')
df.describe().plot(kind='bar', stacked = True)
#12. (3)	A powerpoint file that briefly describes the data set followed by step-by-step analysis results 
#(for each step, code followed by output in screen shots or other image format)