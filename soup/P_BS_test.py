from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

bool = True

#load website to beautiful soup parser
url = 'https://www.tennis.com/rankings/WTA/'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')


#tags for rankings
rankings = bs.find_all('td', {'class':'current-rank'})
#tags for names
names = bs.find_all('td', {'class':'player-name'})
#tags for countries
countries = bs.find_all('span', {'class':'country-name'})
#tags for points
points = bs.find_all('td', {'class':'player-points'})

#Data frame for ranking
r = pd.DataFrame({'rankings':[]})
for ranking in rankings:
    ranking = ranking.get_text()
    rank = {'rankings':ranking}
    r = r.append(rank, ignore_index = True)

#Data frame for name
n = pd.DataFrame({'name':[]})
for name in names:
    name = name.get_text(strip=True)
    nam = {'name':name}
    n = n.append(nam, ignore_index = True)


#Data frame for country
c = pd.DataFrame({'countries':[]})
for country in countries:
    country = country.get_text(strip=True)
    cou = {'countries':country}
    c = c.append(cou, ignore_index = True)


#Data frame for points
p = pd.DataFrame({'points':[]})
for point in points:
    point = point.get_text()
    poi = {'points':point}
    p = p.append(poi, ignore_index = True)

#Concat data frames into one
WTA_1 = pd.concat([r,n,c,p], axis=1, join = 'inner')
#print(WTA_1)


#Getting adress of palyer website
tags = bs.find('tbody').find_all('a')

links = ['https://www.tennis.com/' + tag['href'] for tag in tags]

s = pd.DataFrame({'birthdate': [], 'height': [], 'weight': [], 'plays': [], 'name': []})

#if bool = true scrap only 99 pages
if bool:
    for link in links[:99]:

        try:
            html = request.urlopen(link + 'stats/')
            bs = BS(html.read(), 'html.parser')

            #Birthdate from player stat website
            try:
                birthdate = bs.find('span', {'class':'player-birthdate'}).text
            except:
                birthdate = ''

            #Height from player stat website
            try:
                height = bs.find('span', {'class':'player-height'}).text
                #getting height only in cm (3 numbers)
                height = re.findall('[0-9][0-9][0-9]', height)
            except:
                height = ''

            #Weight from player stat website
            try:
                weight = bs.find('span', {'class':'player-weight'}).text
                #getting weight only in kg (2 numbers, but second stirngs, becaouse first would be first two numbers form Ibs)
                weight = re.findall('[0-9][0-9]', weight)[1:2]
            except:
                weight = ''

            #Plays from player stat website
            try:
                plays = bs.find('span', {'class':'player-plays'}).text
            except:
                plays = ''

            #Name from player stat website
            try:
                name_f = bs.find('span', {'class':'first-name'}).text
                name_l = bs.find('span', {'class':'last-name'}).text
                name = name_f + ' ' + name_l
            except:
                name = ''

            #data frame for these stats
            stats = {'birthdate': birthdate, 'height': height, 'weight': weight, 'plays': plays, 'name': name}
            s = s.append(stats, ignore_index=True)
        except:
            #if there is no link under player name tag
            pass
else:
    for link in links:

        try:
            html = request.urlopen(link + 'stats/')
            bs = BS(html.read(), 'html.parser')

            # Birthdate from player stat website
            try:
                birthdate = bs.find('span', {'class': 'player-birthdate'}).text
            except:
                birthdate = ''

            # Height from player stat website
            try:
                height = bs.find('span', {'class': 'player-height'}).text
                # getting height only in cm (3 numbers)
                height = re.findall('[0-9][0-9][0-9]', height)
            except:
                height = ''

            # Weight from player stat website
            try:
                weight = bs.find('span', {'class': 'player-weight'}).text
                # getting weight only in kg (2 numbers, but second stirngs, becaouse first would be first two numbers form Ibs)
                weight = re.findall('[0-9][0-9]', weight)[1:2]
            except:
                weight = ''

            # Plays from player stat website
            try:
                plays = bs.find('span', {'class': 'player-plays'}).text
            except:
                plays = ''

            # Name from player stat website
            try:
                name_f = bs.find('span', {'class': 'first-name'}).text
                name_l = bs.find('span', {'class': 'last-name'}).text
                name = name_f + ' ' + name_l
            except:
                name = ''

            # data frame for these stats
            stats = {'birthdate': birthdate, 'height': height, 'weight': weight, 'plays': plays, 'name': name}
            s = s.append(stats, ignore_index=True)
        except:
            # if there is no link under player name tag
            pass


WTA_2 = s
#print(WTA_2)

#Merge two dataframes into one on name
WTA = pd.merge(WTA_1, WTA_2, on='name')
print(WTA)

#Saving Data into csv file
WTA.to_csv('WTA_BS_100.csv', index=False)


