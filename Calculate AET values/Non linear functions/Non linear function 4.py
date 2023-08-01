#Non Linear Function 4

def nlf_4(x,a):
  return 1-np.power(x,a)

lower_bound=0.0
upper_bound=10.0

popt,pcov=curve_fit(nlf_4,x,y,bounds=(lower_bound,upper_bound))
a4_fit=popt[0]
print(a4_fit)

df['AET_NLF4_P']=df['PET_P']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_PM']=df['PET_PM']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_PT']=df['PET_PT']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_HS']=df['PET_HS']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_OD']=df['PET_OD']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_Ham']=df['PET_Ham']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_TH']=df['PET_TH']*(1-np.power(1-x,a4_fit))
df['AET_NLF4_BR']=df['PET_BR']*(1-np.power(1-x,a4_fit)
