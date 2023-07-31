from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By

app = Flask(__name__)


def hackerearth_data_scrap () :
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(options=options)
        
        driver.get("https://www.hackerearth.com/@DollarAkshay")

        website = driver.find_element(By.CLASS_NAME,"container")


        elem1 = website.find_element(By.CLASS_NAME, "name")
        elem1_text= elem1.text

        elem2 = website.find_element(By.CLASS_NAME, "gender")
        elem2_text= elem2.text
        

        elem3 = website.find_element(By.CLASS_NAME, "location")
        elem3_text= elem3.text
       

        elem4 = website.find_element(By.CLASS_NAME, "current-position")
        elem4_text= elem4.text
       

        elem5 = website.find_element(By.CLASS_NAME, "education")
        elem5_text= elem5.text
        

        elem6 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[1]/div[2]/div[2]")
        elem6_text= elem6.text
   

        elem7 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div[2]/div[2]")
        elem7_text= elem7.text
       

        elem8 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[3]/div[2]/div[2]")
        elem8_text= elem8.text
        

        elem9 = website.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/div[1]/div/div[3]/div[4]/div[2]/div[2]")
        elem9_text= elem9.text
       

        return {
            "Name": elem1_text,
            "gender" : elem2_text,
            "city" : elem3_text,
            "profession" : elem4_text,
            "education" : elem5_text,
            "points" : elem6_text,
            "Contest Rating" : elem7_text,
            "Problem Solved" : elem8_text,
            "solution submitted" : elem9_text

        }
     
    except Exception as e:
        print ("error", str(e))
        return{}
    
    finally:
        if 'driver' in locals():
            driver.quit()


@app.route('/hackerearth_data', methods=['GET'])
def get_hackerearth_data():
    data = hackerearth_data_scrap()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

    


