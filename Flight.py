from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/travel/flights")

#TravelButton =  WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div/div/div/div/div/div[1]/div/div/div/span[2]/svg")))
#TravelButton.click
#Travelers = input("How many people are on the trip? (provide number only)")
#TravelerNum =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div[2]/div[2]/div[1]/div/button[2]')))
#if TravelerNum > 2:
    #for Traveler in Travelers: 
        #TravelerNum.click
#else:
    #pass

Origin = input("Where is your Origin? (Closest Major City with an Airport) ")
OriginButton =  WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input")))
OriginButton.send_keys(Origin)
OriginButton.send_keys(Keys.TAB)

Destination = input("Where is your Destination? (Closest Major City with an Airport) ")
DesButton =  WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input")))
DesButton.send_keys(Destination)
DesButton.send_keys(Keys.TAB)

StartDate = input("When is your Start Date? (MM/DD/YYYY) ")
SDButton =  WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")))
SDButton.send_keys(StartDate)
SDButton.send_keys(Keys.TAB)

EndDate = input("When is your Return Date? (MM/DD/YYYY) ")
EDButton =  WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input")))
EDButton.send_keys(EndDate)
EDButton.send_keys(Keys.TAB)

time.sleep(10)

Search =  WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button")))
Search.click()

time.sleep(100)