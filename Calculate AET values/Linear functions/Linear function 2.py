#Linear Function 2

def lf_2(pet,a,b):
  return a*np.power(pet,b)

p0=[0.01,0.1]
lower_bound=0.001
upper_bound=1
popt,pcov=curve_fit(lf_2,PET,AET,p0,bounds=[lower_bound,upper_bound])
a=popt[0]
b=popt[1]

print('a :',a)
print('b :',b)

df['AET_PF_P']=a*np.power(df['PET_P'],b)
df['AET_PF_PM']=a*np.power(df['PET_PM'],b)
df['AET_PF_PT']=a*np.power(df['PET_PT'],b)
df['AET_PF_HS']=a*np.power(df['PET_HS'],b)
df['AET_PF_OD']=a*np.power(df['PET_OD'],b)
df['AET_PF_Ham']=a*np.power(df['PET_Ham'],b)
df['AET_PF_TH']=a*np.power(df['PET_TH'],b)
df['AET_PF_BR']=a*np.power(df['PET_BR'],b
