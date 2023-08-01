def Hamon(T):

  PET=1.6169*math.pow(10,-3)*216.7*6.108*(np.exp(17.2693*T/(T+237.3)))*0.35*0.35
  return PET

df['PET_Ham']=Hamon(df['TA_F'])
df['PET_Ham'
