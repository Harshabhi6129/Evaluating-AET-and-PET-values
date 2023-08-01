#Complementary Relationship function 3
#B2015

c=0.12;
df['AET_B2015_P']=(np.power(df['PET_PT']/df['PET_P'],2)*(((2-c)*df['PET_P'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_P']));
df['AET_B2015_PM']=(np.power(df['PET_PT']/df['PET_PM'],2)*(((2-c)*df['PET_PM'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_PM']));
df['AET_B2015_PT']=(np.power(df['PET_PT']/df['PET_PT'],2)*(((2-c)*df['PET_PT'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_PT']));
df['AET_B2015_HS']=(np.power(df['PET_PT']/df['PET_HS'],2)*(((2-c)*df['PET_HS'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_HS']));
df['AET_B2015_OD']=(np.power(df['PET_PT']/df['PET_OD'],2)*(((2-c)*df['PET_OD'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_OD']));
df['AET_B2015_Ham']=(np.power(df['PET_PT']/df['PET_Ham'],2)*(((2-c)*df['PET_Ham'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_Ham']));
df['AET_B2015_TH']=(np.power(df['PET_PT']/df['PET_TH'],2)*(((2-c)*df['PET_TH'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_TH']));
df['AET_B2015_BR']=(np.power(df['PET_PT']/df['PET_BR'],2)*(((2-c)*df['PET_BR'])-((1-2*c)*df['PET_PT'])-c*np.power(df['PET_PT'],2)/df['PET_BR']))
