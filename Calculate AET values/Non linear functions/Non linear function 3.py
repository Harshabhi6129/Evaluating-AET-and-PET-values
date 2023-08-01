#Non Linear Function 3

def nlf_3(x,a):
  return np.power(x,a)

lower_bound=1.0
upper_bound=10.0

popt,pcov=curve_fit(nlf_3,x,y,bounds=(lower_bound,upper_bound))
a3_fit=popt[0]
print(a3_fit)

AET_NLF3_P=df['PET_P']*np.power(x,a3_fit)
df['AET_NLF3_P']=AET_NLF3_P

AET_NLF3_PM=df['PET_PM']*np.power(x,a3_fit)
df['AET_NLF3_PM']=AET_NLF3_PM

AET_NLF3_PT=df['PET_PT']*np.power(x,a3_fit)
df['AET_NLF3_PT']=AET_NLF3_PT

AET_NLF3_HS=df['PET_HS']*np.power(x,a3_fit)
df['AET_NLF3_HS']=AET_NLF3_HS

AET_NLF3_OD=df['PET_OD']*np.power(x,a3_fit)
df['AET_NLF3_OD']=AET_NLF3_OD

AET_NLF3_Ham=df['PET_Ham']*np.power(x,a3_fit)
df['AET_NLF3_Ham']=AET_NLF3_Ham

AET_NLF3_TH=df['PET_TH']*np.power(x,a3_fit)
df['AET_NLF3_TH']=AET_NLF3_TH

AET_NLF3_BR=df['PET_BR']*np.power(x,a3_fit)
df['AET_NLF3_BR']=AET_NLF3_B
