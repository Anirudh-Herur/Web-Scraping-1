from bs4 import BeautifulSoup
import requests
import pandas as pd

link = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')
temp_list = []
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Name = []
Distance = []
Mass = []
Radius = []
Luminosity = []

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(Name, Distance, Mass, Radius, Luminosity)), columns=[
    'Name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
df2.to_csv('bright_stars.csv')
