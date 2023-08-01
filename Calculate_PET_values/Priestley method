def priestley(netrad,T,wind,vpd,g,pa):
  alpha = 1.26

  slope=4098*0.6108*np.exp((17.27*T)/(T+237.3))/((T+237.3)**2)
  PSY = 0.000665*pa

  pet = alpha*(slope*(netrad-g)/2.453*(slope+PSY))

  return pet

df['PET_PT']=priestley(df['NETRAD'],df['TA_F'],df['WS_F'],df['VPD_F'],df['G_F_MDS'],df['PA_F'])
df['PET_PT']
