#Complementary Relationship function 4
#M2015

ε=0.12
df['AET_M2015_P']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_P']);
df['AET_M2015_PM']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_PM']);
df['AET_M2015_PT']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_PT']);
df['AET_M2015_HS']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_HS']);
df['AET_M2015_OD']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_OD']);
df['AET_M2015_Ham']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_Ham']);
df['AET_M2015_TH']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_TH']);
df['AET_M2015_BR']=(1/ε)*(((1+ε)*df['PET_PT'])-df['PET_BR'])

df.to_csv("AET_Values_DataSet.csv",index=False)
