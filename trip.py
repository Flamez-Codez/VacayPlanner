from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def find_top_attractions(city_name):
    driver = webdriver.Chrome()

    driver.get("https://www.google.com/maps")

    try:
       
        search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input")))

        search_bar.clear()
        search_bar.send_keys(f"Top Attractions in {city_name}")
        search_bar.submit()
        search_bar.send_keys(Keys.ENTER)

        input()

        attractions = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]")))

        print(f"Points of Interests in {city_name}:")
        for i, attraction in enumerate(attractions, 1):
            print(f"{i}. {attraction.text}")

    finally:
      
       driver.quit()

city_name = input("Where do you wish to travel? (City/Reigon): ")
find_top_attractions(city_name)