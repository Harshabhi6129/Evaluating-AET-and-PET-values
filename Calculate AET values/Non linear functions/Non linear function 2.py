#Non Linear Function 2

def nlf_2(x,a):
  return np.exp(a*(x-1))

lower_bound=0.0
upper_bound=10.0

popt,pcov=curve_fit(nlf_2,x,y,bounds=(lower_bound,upper_bound))
a2_fit=popt[0]
print(a2_fit)

AET_NLF2_P=df['PET_P']*np.exp(a2_fit*(x-1))
df['AET_NLF2_P']=AET_NLF2_P

AET_NLF2_PM=df['PET_PM']*np.exp(a2_fit*(x-1))
df['AET_NLF2_PM']=AET_NLF2_PM

AET_NLF2_PT=df['PET_PT']*np.exp(a2_fit*(x-1))
df['AET_NLF2_PT']=AET_NLF2_PT

AET_NLF2_HS=df['PET_HS']*np.exp(a2_fit*(x-1))
df['AET_NLF2_HS']=AET_NLF2_HS

AET_NLF2_OD=df['PET_OD']*np.exp(a2_fit*(x-1))
df['AET_NLF2_OD']=AET_NLF2_OD

AET_NLF2_Ham=df['PET_Ham']*np.exp(a2_fit*(x-1))
df['AET_NLF2_Ham']=AET_NLF2_Ham

AET_NLF2_TH=df['PET_TH']*np.exp(a2_fit*(x-1))
df['AET_NLF2_TH']=AET_NLF2_TH

AET_NLF2_BR=df['PET_BR']*np.exp(a2_fit*(x-1))
df['AET_NLF2_BR']=AET_NLF2_B
