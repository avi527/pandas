import pandas as pd

mydata={"name":['bhanu','sudha','puja','rahim'],"salary":[1000,2000,3000,4000],'age':[12,14,15,16]}
df=pd.DataFrame(mydata)
# print(df)

#print top two head using slice
# print(df.head(2))

#print last three head using slice
# print(df.tail(3))


# Merging & Joining :-
# In merging, you can merge two data frames to form a single data frame.
#  You can also decide which columns you want to make common. Let me implement
#   that practically, first I will create three data frames, 
# which has some key-value pairs and then merge the data frames together

mydata1=pd.DataFrame({"name":['bhanu','sudha','puja','rahim'],"salary":[1000,2000,3000,4000],'age':[12,14,15,16]},index=[2001, 2002,2003,2004])
mydata2=pd.DataFrame({"name":['bhanu','sudha','puja','rahim'],"salary":[1000,2000,3000,4000],'age':[12,14,15,16]}, index=[2005, 2006,2007,2008])
dfm=pd.merge(mydata1,mydata2)
#print(dfm,"merging")

#separate columns
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
merged= pd.merge(df1,df2,on ="HPI")
#print(merged)

#combine two differently indexed dataframes into a single result dataframe
df1 = pd.DataFrame({"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
df2 = pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]}, index=[2001, 2003,2004,2004])
joined= df1.join(df2)
#print(joined)

#Concatenation 
# Concatenation basically glues the dataframes together. 
# You can select the dimension on which you want to concatenate.
# For that, just use “pd.concat” and pass in the list of dataframes to concatenate together

df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
concat= pd.concat([df1,df2])
#print(concat)

#specify axix=1
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
concat= pd.concat([df1,df2],axis=1)
print(concat)

#set index
df= pd.DataFrame({"Day":[1,2,3,4], "Visitors":[200, 100,230,300], "Bounce_Rate":[20,45,60,10]}) 
df.set_index("Day", inplace= True)
print(df)