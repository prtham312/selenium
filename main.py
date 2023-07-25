#codechef api
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.codechef.com/users/a0082002avi")




website = driver.find_element(By.CLASS_NAME,"content")

first_h1 = website.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/header/h1")
first_h1_text=first_h1.text

print("Name = " + first_h1_text)

elem = website.find_element(By.CLASS_NAME, 'm-username--link')
elem_text= elem.text
print("Username = " + elem_text)

elem1 = website.find_element(By.CLASS_NAME, 'user-country-name')
elem1_text= elem1.text
print("COUNTRY = " + elem1_text)

elem2 = website.find_element(By.CLASS_NAME, "rating-number")
elem2_text= elem2.text
print("CODECHEF RATING = " + elem2_text)

elem3 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong")
elem3_text=elem3.text

print("Global Ranking = " + elem3_text)

elem4 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[2]/a/strong")
elem4_text=elem4.text
print("Country Ranking = " + elem4_text)

elem5 = website.find_element(By.CLASS_NAME, "games-rating-box-body-text")
elem5_text= elem5.text
print("1V1 Rating = " + elem5_text)

elem6 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[2]/div/div[1]/div[2]/div[2]/p")
elem6_text= elem6.text
print("Puzzle Rating = " + elem6_text)

elem7 = website.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/section[6]/div/h5[1]")
elem7_text= elem7.text
print("Puzzle Rating = " + elem7_text)




driver.quit