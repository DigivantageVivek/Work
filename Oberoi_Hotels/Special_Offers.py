import time
from itertools import count

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import UnexpectedTagNameException

driver = webdriver.Firefox()
driver.implicitly_wait(10)

# open the Oberoi Hotels Website
driver.get("https://www.oberoihotels.com/")

driver.maximize_window()

# Open Offer details URL
driver.find_element(By.XPATH, "//a[@href='https://www.oberoihotels.com/special-offers/']").click()

# Finding offer pages links on the offer details page
links = driver.find_elements(By.CSS_SELECTOR, "a.btn-style1")


# Printing the links

# for link in links:
#     link_url = link.get_attribute("href")
#     if link_url:
#         print(f"URl: {link_url}")

# Function to validate the Urls
def validate_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False


#  Loop for validating each url and printing result
for link in links:
    link_url = link.get_attribute("href")
    if link_url:
        if validate_url(link_url):
            print(f"URL: {link_url} --> Working")
        else:
            print(f"URL: {link_url} --> Not-Working")

# Exit the browser
driver.quit()
