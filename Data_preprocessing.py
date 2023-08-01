import pandas as pd
import numpy as np

df=pd.read_csv("Initial.csv")
df.dtypes
no_value=['SW_IN_F','LW_IN_F','VPD_F','PA_F','WS_F','NETRAD','G_F_MDS','LE_F_MDS','SWC_F_MDS_1','LW_OUT']

for column in no_value:
  df[column]=df[column].replace(-9999,np.NaN)
  mean=int(df[column].mean(skipna=True))
  df[column]=df[column].replace(np.NaN,mean)
  no_zero=['SWC_F_MDS_1_QC']

for column in no_zero:
  df[column]=df[column].replace(0,np.NaN)
  mean=int(df[column].mean(skipna=True))
  df[column]=df[column].replace(np.NaN,mean)
  df['AET_MS']=df['LE_F_MDS']/2.45
df['AET_MS']
df['SWI']=df['SWC_F_MDS_1']/25
df['SWI']
df.to_csv("Initial_DataSet.csv",index=False)
