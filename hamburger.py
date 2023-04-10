from dotenv import load_dotenv
import os 
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


load_dotenv()

url = "https://tabernaburger.deeliv.app/webapp/globais/cardapio/VF5I38"
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
address=os.getenv("ADDRESS")

options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver  = webdriver.Chrome(options=options)
driver.get(url)

actions = ActionChains(driver)


time.sleep(10)

 
driver.quit()
  



   





