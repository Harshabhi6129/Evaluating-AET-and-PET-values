def Thornthwaite(T):
  pi=3.14
  lat=-12.4943
  lat_rad=lat*180/pi
  solar_dec=0.409*np.sin(2*pi-1.39)
  ws=np.arccos(-np.tan(lat_rad)*np.tan(solar_dec))
  N=(24/pi)*ws

  hi=12*np.power(T/5,1.514)
  a=(6.75*(1/np.power(10,7))*np.power(hi,3))-(7.751*(1/np.power(10,5))*(hi**2))+(0.01792*(hi))+(0.49239)
  PET=16*(N/360)*np.power((10*T/hi),a)

  return PET

df['PET_TH']=Thornthwaite(df['TA_F'])
df['PET_TH'
