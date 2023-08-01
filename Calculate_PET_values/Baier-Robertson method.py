#Baier-Robertson Code

def baier_robertson(T,ters_rad):
  Ra=ters_rad
  TD=6
  PET=0.157*T+0.158*TD+0.109*Ra-5.39
  return PET

df['PET_BR']=baier_robertson(df['TA_F'],df['LW_OUT']-df['LW_IN_F'])
df['PET_BR'

df.to_csv("PET_Values_DataSet.csv",index=False)
