from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import  ActionChains
import pytest
from pathlib import Path 
from datetime import date

class Test_OdevClass:
    
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.folderPath = str(date.today()) 
        Path(self.folderPath).mkdir(exist_ok=True) 
        
    def teardown_method(self):
        self.driver.quit()
    
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located(locator))
        
    @pytest.mark.parametrize("username,password", [("1","1"),("kullaniciadim","sifrem")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce"),("problem_user","secret_sauce")])   
    def test_valid_login(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput, username)
        actions.send_keys_to_element(passwordInput, password)
        actions.perform() 
        
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        self.driver.save_screenshot(f"{self.folderPath}/test-valid-login-{username}-{password}.png")
    
    @pytest.mark.parametrize("password", [("secret_sauce")])    
    def test_username_empty(self,password):
        self.waitForElementVisible((By.ID, "password"),7)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        
        errorText = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-username-empty-{password}.png")
        assert errorText.text == "Epic sadface: Username is required" 
    
    @pytest.mark.parametrize("username", [("standard_user"),("problem_user")])    
    def test_password_empty(self,username):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        
        errorText = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-password-empty-{username}.png")
        assert errorText.text == "Epic sadface: Password is required" 
    
    @pytest.mark.parametrize("username,password", [("locked_out_user","secret_sauce")])   
    def test_login_locked(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        errorText = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-login-locked-{username}-{password}.png")
        assert errorText.text == "Epic sadface: Sorry, this user has been locked out." 

    @pytest.mark.parametrize("username,password", [("1","secret_sauce"),("3","secret_sauce")])
    def test_eror_icon(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        errorIcon = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorIcon.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-eror-icon-{username}-{password}.png")

    @pytest.mark.parametrize("username,password", [("problem_user","secret_sauce")])
    def test_login_inventory(self,username,password):
        self.waitForElementVisible((By.ID, "user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        self.waitForElementVisible((By.ID, "password"),7)    
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password) 
        
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
        
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.save_screenshot(f"{self.folderPath}/test-login-inventory-{username}-{password}.png")
    
    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_product_list(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        self.driver.get("https://www.saucedemo.com/inventory.html")
        productList = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.execute_script("window.scrollTo(0,200)") 
        print(f"Ürün : {len(productList)}")
        self.driver.save_screenshot(f"{self.folderPath}/test-product-list-{username}-{password}.png")
     
    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])   
    def test_product_sort(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        productSort = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select")
        productSort.click()
        loHi = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]")
        loHi.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-product-sort-{username}-{password}.png")
        
    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])   
    def test_add_cart(self,username,password):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        
        product1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        product1.click()
        product2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        product2.click()
        product3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        product3.click()
        
        shopping = self.driver.find_element(By.ID, "shopping_cart_container")
        shopping.click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-cart-{username}-{password}.png")
        
    @pytest.mark.parametrize("username,password,firstname,lastname,zip", [("standard_user","secret_sauce","Hümanur","Sağman","123"),("standard_user","secret_sauce","Alperen","Cesur","456"),("standard_user","secret_sauce","Furkan","Ertek","789")])
    def test_information(self,username,password,firstname,lastname,zip):
        self.waitForElementVisible((By.ID, "user-name")) 
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"),7) 
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        shopping = self.driver.find_element(By.ID, "shopping_cart_container")
        shopping.click()
        checkOut = self.driver.find_element(By.ID, "checkout")
        checkOut.click()
        
        self.waitForElementVisible((By.ID, "first-name")) 
        firstnameInput = self.driver.find_element(By.ID, "first-name")
        self.waitForElementVisible((By.ID, "last-name")) 
        lastnameInput = self.driver.find_element(By.ID, "last-name")
        self.waitForElementVisible((By.ID, "postal-code")) 
        zipInput = self.driver.find_element(By.ID, "postal-code")
        firstnameInput.send_keys(firstname)
        lastnameInput.send_keys(lastname)
        zipInput.send_keys(zip)
        self.driver.save_screenshot(f"{self.folderPath}/test-information-{firstname}-{lastname}.png")
