from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class testSauce:

    # kullanıcı adı ve şifre boş olduğunda alınan uyarı
    def kullaniciAdiBos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        kullaniciGiris = driver.find_element(By.ID, "userName")
        sifreGiris = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "loginButton")
        loginButton.click()
        errorText = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testSonuc = errorText.text == "Epic sadface: Username is required" 
        print(f"sonuç: {testSonuc}")
        sleep(10)
    

    def sifreBos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        kullaniciGiris = driver.find_element(By.ID, "userName")
        sifreGiris = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "loginButton")
        loginButton.click()
        errorText = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testSonuc = errorText.text == "Epic sadface: Password is required" 
        print(f"sonuç: {testSonuc}")
        sleep(10)

    def girisKitlendi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        kullaniciGiris = driver.find_element(By.ID, "userName")
        sifreGiris = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "loginButton")
        loginButton.click()
        errorText = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testSonuc = errorText.text == "Epic sadface: Sorry, this user has been locked out." 
        print(f"sonuç: {testSonuc}")
        sleep(100)

    def errorIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        kullaniciGiris = driver.find_element(By.ID, "userName")
        sifreGiris = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "loginButton")
        loginButton.click()
        errorIcon = driver.find_element(By.CLASS_NAME, "errorButton")
        errorIcon.click()
        sleep(10)


    def girisBilgileri(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        kullaniciGiris = driver.find_element(By.ID, "userName")
        kullaniciGiris.send_keys("problem_user")   
        sifreGiris = driver.find_element(By.ID, "password")
        sifreGiris.send_keys("secret_sauce") 
        loginButton = driver.find_element(By.ID, "loginButton")
        loginButton.click()
        sleep(10)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(100)
    

    #  ürün sayısını ekrana veren fonksiyon
    def urunListesi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        sleep(10)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")   
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce") 
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(10)
        driver.get("https://www.saucedemo.com/inventory.html")
        productList = driver.find_elements(By.CLASS_NAME, "inventory_item") 
        print(f"Ürün : {len(productList)}")
        sleep(100)


testSauce = testSauce()

testSauce.kullaniciAdiBos() 
testSauce.sifreBos()
testSauce.girisKitlendi()
testSauce.errorIcon()
testSauce.girisBilgileri()
testSauce.urunListesi()


while True:
    continue
