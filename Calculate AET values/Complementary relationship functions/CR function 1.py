#Complementary Relationship function 1
#B1963

df['AET_B1963_P']=2*(df['PET_PT'])-df['PET_P'];
df['AET_B1963_PM']=2*(df['PET_PT'])-df['PET_PM'];
df['AET_B1963_PT']=2*(df['PET_PT'])-df['PET_PT'];
df['AET_B1963_HS']=2*(df['PET_PT'])-df['PET_HS'];
df['AET_B1963_OD']=2*(df['PET_PT'])-df['PET_OD'];
df['AET_B1963_Ham']=2*(df['PET_PT'])-df['PET_Ham'];
df['AET_B1963_TH']=2*(df['PET_PT'])-df['PET_TH'];
df['AET_B1963_BR']=2*(df['PET_PT'])-df['PET_BR'];
