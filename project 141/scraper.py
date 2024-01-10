import requests
from bs4 import BeautifulSoup
import pandas as pd

START_URL = 'https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&oldid=945771782'
headers = ["Name", "Distance", "Mass", "Radius"]

page = requests.get(START_URL)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

stars_data = []

for row in rows[1:]:
    columns = row.find_all('td')
    name = columns[1].text.strip()
    distance = columns[3].text.strip()
    mass = columns[5].text.strip()
    radius = columns[6].text.strip()
    
    star_info = {
        "Name": name,
        "Distance": distance,
        "Mass": mass,
        "Radius": radius
    }
    
    stars_data.append(star_info)

planet_df = pd.DataFrame(stars_data, columns=headers)
planet_df.to_csv("brightest_stars_data.csv", index=False)
