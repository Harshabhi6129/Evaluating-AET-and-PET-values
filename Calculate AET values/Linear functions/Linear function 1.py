#Linear Function 1

def linear(AET,PET):
  mean_aet=np.mean(AET)
  mean_pet=np.mean(PET)
  a5=mean_aet/mean_pet
  return a5*PET


df['AET_lf_P']=linear(AET,df['PET_P'])
df['AET_lf_PM']=linear(AET,df['PET_PM'])
df['AET_lf_PT']=linear(AET,df['PET_PT'])
df['AET_lf_HS']=linear(AET,df['PET_HS'])
df['AET_lf_OD']=linear(AET,df['PET_OD'])
df['AET_lf_Ham']=linear(AET,df['PET_Ham'])
df['AET_lf_TH']=linear(AET,df['PET_TH'])
df['AET_lf_BR']=linear(AET,df['PET_BR']
