from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/w/index.php?title=List_of_brightest_stars_and_other_record_stars&amp/"


browser = webdriver.Chrome("C:/Users/smith/OneDrive/Desktop/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "stars"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index , li_tag in enumerate(li_tags):
                if index ==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

        

                    
        



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "how bright", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
stars_df_1 =  pd.DataFrame(stars_data,columns=headers)

# Convert to CSV
stars_df_1.to_csv("scrapdata.csv", index=True, index_label="id")
    


