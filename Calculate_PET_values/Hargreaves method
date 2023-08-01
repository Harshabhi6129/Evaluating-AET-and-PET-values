def Hargreaves(T,ters_rad,wind):

  Ra=ters_rad
  #pet = (0.0023*Rs*math.sqrt(8)*(T+b))/(2.501-0.002361*T)
  pet=0.0135*(T+17.8)*Ra*0.408*0.19*np.sqrt(6)

  return pet

df['PET_HS']=Hargreaves(df['TA_F'],df['LW_OUT']-df['LW_IN_F'],df['WS_F'])
df['PET_HS']
