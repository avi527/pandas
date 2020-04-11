import pandas as pd
import numpy as np

s=pd.Series()
print(s)

#We did not pass any index, so by default, it assigned the indexes ranging from 0 to len(data)-1
data=np.array(['a','b','c'])
data_ind=pd.Series(data)
print(data_ind)

#if we pass data index then how to set index with data
#We passed the index values here. Now we can see the customized indexed values in the output.

data=np.array(['a','v','d','g','n'])
set_index_withdata=pd.Series(data,index=[100,101,102,103,104])
print(set_index_withdata)

#Dictionary keys are used to construct index

data={'a':0.,'b':1.,'c':2}
s=pd.Series(data)
print(s)

#Index order is persisted and the missing element is filled with NaN (Not a Number).
data={'a':0.,'b':1.,'c':2}
set_index=pd.Series(data,index=['c','a','b','e'])
print(set_index)

#Accessing Data from Series with Position
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first element
print (s[0])

s1 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the first three element
print (s1[:3])

s2 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve the last three element
print (s2[-3:])

#A Series is like a fixed-size dict in that you can get and set values by index label.
s3 = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve a single element
print (s3['a'])


s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
#retrieve multiple elements
print (s[['a','c','d']])