from selenium import webdriver
import pandas as pd

#if bool = True program scrap 100 pages
bool = True

#insert your geckodriver path here:
gecko_path = 'C:\selenium browser driver\geckodriver.exe'

url = 'https://www.tennis.com/rankings/WTA/'

options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox(options = options, executable_path = gecko_path)

driver.get(url)

#Data frame for ranking
r = pd.DataFrame({'rankings':[]})
rankings = driver.find_elements_by_xpath('//tbody/tr/td[1]')
for ranking in rankings:
    ranking = ranking.text
    rank = {'rankings':ranking}
    r = r.append(rank, ignore_index = True)

#Data frame for name
n = pd.DataFrame({'name':[]})
names = driver.find_elements_by_xpath('//tbody/tr/td[3]')
for name in names:
    name = name.text
    nam = {'name': name}
    n = n.append(nam, ignore_index=True)

#Data frame for country
c = pd.DataFrame({'countries':[]})
countries = driver.find_elements_by_xpath('//tbody/tr/td[4]/span')
for country in countries:
    country = country.text
    cou = {'countries':country}
    c = c.append(cou, ignore_index = True)

#Data frame for points
p = pd.DataFrame({'points':[]})
points = driver.find_elements_by_xpath('//tbody/tr/td[5]')
for point in points:
    point = point.text
    poi = {'points': point}
    p = p.append(poi, ignore_index=True)



#Links for next driver
names_l=[]
names = driver.find_elements_by_xpath('//tbody/tr/td[3]/a')
for name in names:
    names_l.append(name.get_attribute("href"))
#print(names_l)


b = pd.DataFrame({'birthdate':[]})
h = pd.DataFrame({'height':[]})
w = pd.DataFrame({'weight':[]})
pl = pd.DataFrame({'plays':[]})
na = pd.DataFrame({'name':[]})

if bool:
    for name_l in names_l[:99]:
        try:
            driver.get(name_l)
            #if page has sub-page 'stats' open it
            try:
                stats = driver.find_element_by_xpath('/html/body/section/div[1]/div[1]/div[2]/ul/li[2]/a')
                stats.click()

                #scraping birth date
                try:
                    birthdate = driver.find_element_by_xpath('//div/ul[2]/li[1]/span')
                    birthdate = birthdate.text
                    bir = {'birthdate': birthdate}
                    b = b.append(bir, ignore_index=True)
                except:
                    bir = {'birthdate': ''}
                    b = b.append(bir, ignore_index=True)

                #scraping height
                try:
                    height = driver.find_element_by_xpath('//div/ul[2]/li[2]/span')
                    height = height.text
                    height = height[height.find('(')+1:height.find('c')-1]

                    hei = {'height': height}
                    h = h.append(hei, ignore_index=True)
                except:
                    hei = {'height': ''}
                    h = h.append(hei, ignore_index=True)

                #scraping weight
                try:
                    weight = driver.find_element_by_xpath('//div/ul[2]/li[3]/span')
                    weight = weight.text
                    weight = weight[weight.find('(') + 1:weight.find('k') - 1]

                    wei = {'weight': weight}
                    w = w.append(wei, ignore_index=True)
                except:
                    wei = {'weight': ''}
                    w = w.append(wei, ignore_index=True)

                #scraping plays
                try:
                    play = driver.find_element_by_xpath('//div/ul[2]/li[4]/span')
                    play = play.text
                    pla = {'plays': play}
                    pl = pl.append(pla, ignore_index=True)
                except:
                    pla = {'plays': ''}
                    pl = pl.append(pla, ignore_index=True)

                #scraping name
                try:
                    # first name
                    name_f = driver.find_element_by_xpath('//h3/span[1]')
                    name_f = name_f.text
                    # second name
                    name_s = driver.find_element_by_xpath('//h3/span[2]')
                    name_s = name_s.text
                    #full name
                    name = name_f + ' ' + name_s
                    nam = {'name': name}
                    na = na.append(nam, ignore_index=True)
                except:
                    nam = {'name': ''}
                    na = na.append(nam, ignore_index=True)

            #if page doesn't have stats page
            except:

                #scraping birth date
                try:
                    birthdate = driver.find_element_by_xpath('//div/ul[2]/li[1]/span')
                    birthdate = birthdate.text
                    bir = {'birthdate': birthdate}
                    b = b.append(bir, ignore_index=True)
                except:
                    bir = {'birthdate': ''}
                    b = b.append(bir, ignore_index=True)

                #scraping height
                try:
                    height = driver.find_element_by_xpath('//div/ul[2]/li[2]/span')
                    height = height.text
                    height = height[height.find('(')+1:height.find('c')-1]

                    hei = {'height': height}
                    h = h.append(hei, ignore_index=True)
                except:
                    hei = {'height': ''}
                    h = h.append(hei, ignore_index=True)

                #scraping weight
                try:
                    weight = driver.find_element_by_xpath('//div/ul[2]/li[3]/span')
                    weight = weight.text
                    weight = weight[weight.find('(') + 1:weight.find('k') - 1]

                    wei = {'weight': weight}
                    w = w.append(wei, ignore_index=True)
                except:
                    wei = {'weight': ''}
                    w = w.append(wei, ignore_index=True)

                #scraping plays
                try:
                    play = driver.find_element_by_xpath('//div/ul[2]/li[4]/span')
                    play = play.text
                    pla = {'plays': play}
                    pl = pl.append(pla, ignore_index=True)
                except:
                    pla = {'plays': ''}
                    pl = pl.append(pla, ignore_index=True)

                #scraping name
                try:
                    # first name
                    name_f = driver.find_element_by_xpath('//h3/span[1]')
                    name_f = name_f.text
                    # second name
                    name_s = driver.find_element_by_xpath('//h3/span[2]')
                    name_s = name_s.text
                    # full name
                    name = name_f + ' ' + name_s
                    nam = {'name': name}
                    na = na.append(nam, ignore_index=True)
                except:
                    nam = {'name': ''}
                    na = na.append(nam, ignore_index=True)

            # go back to the previous website
            driver.get(url)
        except:
            pass
else:
    for name_l in names_l:
        try:
            driver.get(name_l)
            #if page has sub-page 'stats' open it
            try:
                stats = driver.find_element_by_xpath('/html/body/section/div[1]/div[1]/div[2]/ul/li[2]/a')
                stats.click()

                #scraping birth date
                try:
                    birthdate = driver.find_element_by_xpath('//div/ul[2]/li[1]/span')
                    birthdate = birthdate.text
                    bir = {'birthdate': birthdate}
                    b = b.append(bir, ignore_index=True)
                except:
                    bir = {'birthdate': ''}
                    b = b.append(bir, ignore_index=True)

                #scraping height
                try:
                    height = driver.find_element_by_xpath('//div/ul[2]/li[2]/span')
                    height = height.text
                    height = height[height.find('(')+1:height.find('c')-1]

                    hei = {'height': height}
                    h = h.append(hei, ignore_index=True)
                except:
                    hei = {'height': ''}
                    h = h.append(hei, ignore_index=True)

                #scraping weight
                try:
                    weight = driver.find_element_by_xpath('//div/ul[2]/li[3]/span')
                    weight = weight.text
                    weight = weight[weight.find('(') + 1:weight.find('k') - 1]

                    wei = {'weight': weight}
                    w = w.append(wei, ignore_index=True)
                except:
                    wei = {'weight': ''}
                    w = w.append(wei, ignore_index=True)

                #scraping plays
                try:
                    play = driver.find_element_by_xpath('//div/ul[2]/li[4]/span')
                    play = play.text
                    pla = {'plays': play}
                    pl = pl.append(pla, ignore_index=True)
                except:
                    pla = {'plays': ''}
                    pl = pl.append(pla, ignore_index=True)

                #scraping name
                try:
                    # first name
                    name_f = driver.find_element_by_xpath('//h3/span[1]')
                    name_f = name_f.text
                    # second name
                    name_s = driver.find_element_by_xpath('//h3/span[2]')
                    name_s = name_s.text
                    # full name
                    name = name_f + ' ' + name_s
                    nam = {'name': name}
                    na = na.append(nam, ignore_index=True)
                except:
                    nam = {'name': ''}
                    na = na.append(nam, ignore_index=True)

            #if page doesn't have stats page
            except:

                #scraping birth date
                try:
                    birthdate = driver.find_element_by_xpath('//div/ul[2]/li[1]/span')
                    birthdate = birthdate.text
                    bir = {'birthdate': birthdate}
                    b = b.append(bir, ignore_index=True)
                except:
                    bir = {'birthdate': ''}
                    b = b.append(bir, ignore_index=True)

                #scraping height
                try:
                    height = driver.find_element_by_xpath('//div/ul[2]/li[2]/span')
                    height = height.text
                    height = height[height.find('(')+1:height.find('c')-1]

                    hei = {'height': height}
                    h = h.append(hei, ignore_index=True)
                except:
                    hei = {'height': ''}
                    h = h.append(hei, ignore_index=True)

                #scraping weight
                try:
                    weight = driver.find_element_by_xpath('//div/ul[2]/li[3]/span')
                    weight = weight.text
                    weight = weight[weight.find('(') + 1:weight.find('k') - 1]

                    wei = {'weight': weight}
                    w = w.append(wei, ignore_index=True)
                except:
                    wei = {'weight': ''}
                    w = w.append(wei, ignore_index=True)

                #scraping plays
                try:
                    play = driver.find_element_by_xpath('//div/ul[2]/li[4]/span')
                    play = play.text
                    pla = {'plays': play}
                    pl = pl.append(pla, ignore_index=True)
                except:
                    pla = {'plays': ''}
                    pl = pl.append(pla, ignore_index=True)

                #scraping name
                try:
                    #first name
                    name_f = driver.find_element_by_xpath('//h3/span[1]')
                    name_f = name_f.text
                    #secend name
                    name_s = driver.find_element_by_xpath('//h3/span[2]')
                    name_s = name_s.text
                    #full name
                    name = name_f + ' ' + name_s
                    nam = {'name': name}
                    na = na.append(nam, ignore_index=True)
                except:
                    nam = {'name': ''}
                    na = na.append(nam, ignore_index=True)

            # go back to the previous website
            driver.get(url)
        except:
            pass


WTA_s = pd.concat([b,h,w,pl,na], axis=1, join = 'inner')
#print(WTA_s)

WTA_r = pd.concat([r,n,c,p], axis=1, join = 'inner')
#print(WTA_r)

WTA = pd.merge(WTA_r, WTA_s, on='name')
#print(WTA)

#Ssaving Data into csv file
WTA.to_csv('WTA_selenium_100.csv', index=False)

# Close browser:
driver.quit()
