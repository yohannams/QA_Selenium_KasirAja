import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):  # TC1
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys(
            "yohannams@yahoo.com"
        )  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("123456")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "chakra-heading").text
        self.assertIn("kasirAja", response_data)

    def test_a_failed_login(self):  # TC2
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys(
            "yohannams@yahoo.com"
        )  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("111111")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "chakra-alert").text
        self.assertIn("Kredensial yang Anda berikan salah", response_data)

    def test_a_failed_login_empty_password(self):  # TC3
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys(
            "yohannams@yahoo.com"
        )  # isi email
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "chakra-alert").text
        self.assertIn('"password" is not allowed to be empty', response_data)

    def test_a_success_logout(self):  # TC4
        # steps
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(3)
        driver.find_element(By.ID, "email").send_keys(
            "yohannams@yahoo.com"
        )  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("123456")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu-button-14").click()
        time.sleep(1)
        driver.find_element(By.ID, "menu-list-14-menuitem-12").click()

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
