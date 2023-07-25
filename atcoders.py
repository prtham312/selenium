#codewars api
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.hackerearth.com/@DollarAkshay")

website = driver.find_element(By.CLASS_NAME,"container")


elem1 = website.find_element(By.CLASS_NAME, "name")
elem1_text= elem1.text
print("Name = " + elem1_text)

elem2 = website.find_element(By.CLASS_NAME, "gender")
elem2_text= elem2.text
print("gender = " + elem2_text)

elem3 = website.find_element(By.CLASS_NAME, "location")
elem3_text= elem3.text
print("city = " + elem3_text)

elem4 = website.find_element(By.CLASS_NAME, "current-position")
elem4_text= elem4.text
print("profession = " + elem4_text)

elem5 = website.find_element(By.CLASS_NAME, "education")
elem5_text= elem5.text
print("education = " + elem5_text)

elem6 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]")
elem6_text= elem6.text
print("Points = " + elem6_text)

elem7 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]")
elem7_text= elem7.text
print("Contest ratings = " + elem7_text)

elem8 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[3]/div[2]/div[2]")
elem8_text= elem8.text
print("Problem solved = " + elem8_text)

elem9 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[4]/div[2]/div[2]")
elem9_text= elem9.text
print("Solutions submitted = " + elem9_text)




driver.quit

