import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import baseLogin
from selenium.webdriver.common.keys import Keys


class TestPembelian(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_failed_search(self):  # TC19
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/purchases"]').click()
        time.sleep(1)
        element = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-d4ejuc']/div[1]/div[@class='chakra-input__group css-4302v8']/input[@value='2023-5-20']",
        )
        is_disabled = element.is_enabled()
        self.assertFalse(is_disabled)

    def test_a_success_add_pembelian(self):  # TC20
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/purchases"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/purchases/create"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[6]",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody[@class='css-0']/tr[@role='row']/td[4]/input[@value='1']",
        ).send_keys(
            "2"
        )  # isi jumlah
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-zebbu0']/div[@class='css-j7qwjs']/div[@class='css-0']/button[@type='button']",
        ).click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def test_a_success_add_pembelian_invalid_jumlah(self):  # TC21
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/purchases"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/purchases/create"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[6]",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody[@class='css-0']/tr[@role='row']/td[4]/input[@value='1']",
        ).send_keys(
            Keys.CONTROL + "a"
        )  # Memilih seluruh teks
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody[@class='css-0']/tr[@role='row']/td[4]/input[@value='1']",
        ).send_keys(
            "0"
        )  # isi jumlah
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-zebbu0']/div[@class='css-j7qwjs']/div[@class='css-0']/button[@type='button']",
        ).click()  # simpan
        time.sleep(1)
        driver.find_element(By.ID, "chakra-alert")

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
