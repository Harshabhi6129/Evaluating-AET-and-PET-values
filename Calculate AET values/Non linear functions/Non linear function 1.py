#Non Linear Function 1

def nlf_1(x,a):
  return np.power(a,x-1)

lower_bound=1.0
upper_bound=10.0

popt,pcov=curve_fit(nlf_1,x,y,bounds=(lower_bound,upper_bound))
a1_fit=popt[0]
print('a1 : ',a1_fit)

AET_NLF1_P=df['PET_P']*np.power(a1_fit,x-1)
df['AET_NLF1_P']=AET_NLF1_P

AET_NLF1_PM=df['PET_PM']*np.power(a1_fit,x-1)
df['AET_NLF1_PM']=AET_NLF1_PM

AET_NLF1_PT=df['PET_PT']*np.power(a1_fit,x-1)
df['AET_NLF1_PT']=AET_NLF1_PT

AET_NLF1_HS=df['PET_HS']*np.power(a1_fit,x-1)
df['AET_NLF1_HS']=AET_NLF1_HS

AET_NLF1_OD=df['PET_OD']*np.power(a1_fit,x-1)
df['AET_NLF1_OD']=AET_NLF1_OD

AET_NLF1_Ham=df['PET_Ham']*np.power(a1_fit,x-1)
df['AET_NLF1_Ham']=AET_NLF1_Ham

AET_NLF1_TH=df['PET_TH']*np.power(a1_fit,x-1)
df['AET_NLF1_TH']=AET_NLF1_TH

AET_NLF1_BR=df['PET_BR']*np.power(a1_fit,x-1)
df['AET_NLF1_BR']=AET_NLF1_B
