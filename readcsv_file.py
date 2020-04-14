import pandas as pd

read_file=pd.read_csv('datacsv.csv')
#print(read_file)
# help(pd.read_csv)

read_file=pd.read_csv('datacsv.csv',usecols=[0,2,3])
#print(read_file)

read_file_index1=pd.read_csv('datacsv.csv',usecols=[1])
#print(read_file_index1)

#skip rows
read_csvfile=pd.read_csv('datacsv.csv',skiprows=[1,3])
#print(read_csvfile)

#index_col method
read_csvfile=pd.read_csv('datacsv.csv',index_col='first_name')
#print(read_csvfile)

#header method
head_csvfile=pd.read_csv('datacsv.csv',header=1)
#print(head_csvfile)

#prefix function
head_csvfile_prefix=pd.read_csv('datacsv.csv',prefix="haa",header=None)
print(head_csvfile_prefix)


