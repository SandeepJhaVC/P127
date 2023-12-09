import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

# Initialize the webdriver
driver = webdriver.Chrome()


url = "https://en.wikipedia.org/wiki/List_of_proper_names_of_stars"


driver.get(url)


time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'html.parser')


all_rows = soup.find_all('tr')


scraped_data = []


def scrape_row(row):
    columns = row.find_all('td')
    if len(columns) >= 5:

        temp_list = []
        

        temp_list.append(columns[0].text.strip())
        temp_list.append(columns[1].text.strip())
        temp_list.append(columns[2].text.strip())
        temp_list.append(columns[3].text.strip())
        temp_list.append(columns[4].text.strip())

        return temp_list


for row in all_rows:
   
    star_data = scrape_row(row)
    if star_data:

        scraped_data.append(star_data)


df = pd.DataFrame(scraped_data, columns=['Star Name', 'Distance', 'Mass', 'Radius', 'Luminosity'])


df.to_csv('stars_data.csv', index=False)


print(df)
