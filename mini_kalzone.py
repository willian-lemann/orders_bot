import os 
from dotenv import load_dotenv
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

load_dotenv()

url = "https://maisdeliveryapp.com.br/pwa/#/dashboard/user/request"
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
address = os.getenv("ADDRESS")

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver  = webdriver.Chrome(options=options)
driver.get(url)

actions = ActionChains(driver)

time.sleep(2)

def chossing_state_city():
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]/div/ul/li[25]/ul/li").click()
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[4]/div/div[2]/div/ul/li[12]/ul/li").click()

def do_login():
   time.sleep(4)
   driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/div[3]/div").click()
   time.sleep(3)

def fill_form():
   driver.find_element(By.NAME, "user_name").click()
   driver.find_element(By.NAME, "user_name").send_keys(email)
   driver.find_element(By.NAME, "user_password").click()
   driver.find_element(By.NAME, "user_password").send_keys(password)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[2]/form/button").click()

def make_order():
   def click_next_button():
      driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/button").click()   

   #kalzone
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/input").click()
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/input").send_keys("Mini Kalzone")
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/input").send_keys(Keys.ENTER)
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[3]/div/div").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[3]/div").click()
   time.sleep(1)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[4]/input").click()
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[4]/input").send_keys("Frango")
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div[2]/div").click()
   time.sleep(1)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div/button").click()
   time.sleep(1)
   click_next_button()
   time.sleep(2)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[4]/button").click()
   print("Frango chose..")
   time.sleep(3)

   # mega ligado
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[3]/div").click()
   time.sleep(1)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[4]/input").click()
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[4]/input").send_keys("Mega Ligado")
   time.sleep(3)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[3]/div[1]/div").click()
   time.sleep(5)
   driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/div/button").click()
   time.sleep(2)
   print("Mega Ligado chose..")
   click_next_button()
   time.sleep(2)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/button").click()
   time.sleep(5)
   actions.move_by_offset(400, 570)
   time.sleep(3)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[6]/div[2]/textarea").send_keys(address)
   time.sleep(3)
   total = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[4]/div[2]/h3[2]").text
   print(f"Frango and Mega Ligado ordered successfully! Total will be {total}")
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[7]/button").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/button").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/ul/li[2]/ul/li").click()
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[5]").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/ul/li[2]/ul/li").click()
   time.sleep(2)
   driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div[7]/button").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[3]/button").click()
   time.sleep(4)

print("Entering Mais Delivery..")
chossing_state_city()
print("Entering in platform..")
do_login()
print("Signin in..")
fill_form()
print("Making order..")
make_order()
driver.quit()
  



   





