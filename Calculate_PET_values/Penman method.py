import numpy as np
import pandas as pd
import math
df=pd.read_csv("Initial_DataSet.csv")
df.dtypes
no_value=['LW_OUT']

for column in no_value:
  df[column]=df[column].replace(-9999,np.NaN)
  mean=int(df[column].mean(skipna=True))
  df[column]=df[column].replace(np.NaN,mean)

//Penman
def penman(Rn,T,wind,vpd,g,pa):

  #calculate psychrometric constant
  PSY = 0.000665*pa

  #calculate slope of vapor pressure curve
  slope=4098*(0.6108*np.exp((17.27*T)/(T+237.3)))/((T+237.3)**2)

  #calculate PET
  pet=(slope*(Rn-g)+6.43*PSY*(1+0.536*wind)*vpd)/((2.501-0.00236*T)*(slope+PSY))

  return pet/28.9

df['PET_P']=penman(df['NETRAD'],df['TA_F'],df['WS_F'],df['VPD_F'],df['G_F_MDS'],df['PA_F'])
df['PET_P']
