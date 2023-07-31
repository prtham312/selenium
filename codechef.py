from flask import Flask,jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)

def codechef_data_scrap():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.codechef.com/users/a0082002avi")




        website = driver.find_element(By.CLASS_NAME,"content")

        first_h1 = website.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/header/h1")
        first_h1_text=first_h1.text

       
        elem = website.find_element(By.CLASS_NAME, 'm-username--link')
        elem_text= elem.text
       
        elem1 = website.find_element(By.CLASS_NAME, 'user-country-name')
        elem1_text= elem1.text
        

        elem2 = website.find_element(By.CLASS_NAME, "rating-number")
        elem2_text= elem2.text
        

        elem3 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[1]/a/strong")
        elem3_text=elem3.text

        

        elem4 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[1]/div/div[2]/ul/li[2]/a/strong")
        elem4_text=elem4.text
       

        elem5 = website.find_element(By.CLASS_NAME, "games-rating-box-body-text")
        elem5_text= elem5.text
        
        elem6 = website.find_element(By.XPATH, "/html/body/main/div/div/div/aside/div[2]/div/div[1]/div[2]/div[2]/p")
        elem6_text= elem6.text
        

        elem7 = website.find_element(By.XPATH, "/html/body/main/div/div/div/div/div/section[6]/div/h5[1]")
        elem7_text= elem7.text
        

        return{
             "Name": first_h1_text,
            "username" : elem_text,
            "country" : elem1_text,
            "codechef rating" : elem2_text,
            "global ranking" : elem3_text,
            "country ranking" : elem4_text,
            "1V1 rating" : elem5_text,
            "Puzzle rating" : elem6_text,
            "fully solved" : elem7_text
        }


    except Exception as e:
            print ("error", str(e))
            return{}

    finally:
        if 'driver' in locals():
            driver.quit

@app.route('/codechef_data', methods=['GET'])
def get_codechef_data():
    data = codechef_data_scrap()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)