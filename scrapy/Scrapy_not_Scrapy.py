import pandas as pd

wta_2 = pd.read_csv('WTA2.csv')
#print(wta_2)
wta_3 = pd.read_csv('WTA3.csv')
#print(wta_3)

#merge two csv into one on name
wta = pd.merge(wta_2, wta_3, on='name')
#print(wta)

#Ssaving Data into csv file
wta.to_csv('WTA_Scrapy.csv', index=False)