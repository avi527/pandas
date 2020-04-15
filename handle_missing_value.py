import pandas as pd

mydata=pd.read_csv('datacsv.csv')
print(mydata.isnull())
print(mydata.isnull().sum())
print(mydata.isnull().sum().sum())
print(mydata.notnull())
print(mydata.notnull().sum())
print(mydata.notnull().sum().sum())

# #dropna method()
data=pd.read_csv('datacsv.csv')
print(data.dropna())
print(data.dropna(axis=1))
howdata=data.dropna(how='all')
print(howdata)
print(data.dropna(thresh=4))
print(data.dropna(inplace=True))

#Pandas Append() Function
d1=pd.DataFrame({'a':[2,3,4,5],'b':[9,8,7,6]})
d2=pd.DataFrame({'a':[6,5,4,3],'b':[3,5,4,6]})
#print(d1,d2)
df_append=d1.append(d2)
print(df_append)




