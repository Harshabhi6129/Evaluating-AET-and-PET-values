#Complementary Relationship function 2
#G1989

#calculate psychrometric constant
PSY = 0.000665*df['PA_F']

T=df['TA_F']
#calculate slope of vapor pressure curve
slope=4098*(0.6108*np.exp((17.27*T)/(T+237.3)))/((T+237.3)**2)

# CR METHODS
df['AET_G1989_P']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_P']);
df['AET_G1989_PM']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_PM']);
df['AET_G1989_PT']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_PT']);
df['AET_G1989_HS']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_HS']);
df['AET_G1989_OD']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_OD']);
df['AET_G1989_Ham']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_Ham']);
df['AET_G1989_TH']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_TH']);
df['AET_G1989_BR']=(((PSY + slope)/PSY)*(df['PET_PT']))-(PSY/slope)*(df['PET_BR'])
