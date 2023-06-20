import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_a_success_login(driver):
    # steps
    driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
    time.sleep(3)
    driver.find_element(By.ID, "email").send_keys("yohannams@yahoo.com")  # isi email
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("123456")  # isi password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "chakra-button").click()
    time.sleep(1)
