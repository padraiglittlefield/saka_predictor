# from splinter import Browser
# import requests


# chromedriver = "data\chromedriver"
# ## go to original page 
# browser = Browser(chromedriver)
# browser.visit("https://fbref.com/en/comps/9/2022-2023/stats/2022-2023-Premier-League-Stats")

from selenium import webdriver

chromedriver = 'C:\\Users\\Student\\saka_predictor\\data\\data\\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get("https://fbref.com/en/comps/9/2022-2023/stats/2022-2023-Premier-League-Stats")
