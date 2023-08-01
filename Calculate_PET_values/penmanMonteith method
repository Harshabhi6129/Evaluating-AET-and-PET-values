def penmanMonteith(Rn,T,wind,vpd,g,pa):

  slope=4098*(0.6108*np.exp((17.27*T)/(T+237.3)))/((T+237.3)**2)
  PSY = 0.000665*pa

  num = 0.408*slope*(Rn-g)+PSY*(900/(T+273.15))*wind*vpd
  den = slope+PSY*(1+0.34*wind)

  pet = num/den

  return pet/28.9

df['PET_PM']=penmanMonteith(df['NETRAD'],df['TA_F'],df['WS_F'],df['VPD_F'],df['G_F_MDS'],df['PA_F'])
df['PET_PM']
