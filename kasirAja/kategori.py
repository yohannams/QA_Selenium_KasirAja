import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import baseLogin
from selenium.webdriver.common.keys import Keys


class TestKategori(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_kategori(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("makanan")  # isi nama
        driver.find_element(By.ID, "deskripsi").send_keys("snack")  # isi deskripsi
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        response_data = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//table[@role='table']/tbody/tr[1]/td[1]",
        ).text
        self.assertIn("makanan", response_data)

    def test_a_success_add_kategori_empty_deskripsi(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("minuman")  # isi nama
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        response_data = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//table[@role='table']/tbody/tr[1]/td[1]",
        ).text
        self.assertIn("minuman", response_data)

    def test_a_success_edit_kategori(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[2]/td[3]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[2]/td[3]//div[@role='menu']/a[@role='menuitem']",
        ).click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys(" ringan")  # isi nama
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def test_a_success_delete_kategori(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/categories"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[2]/td[3]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[2]/td[3]//div[@role='menu']/button[@role='menuitem']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']/div[@class='chakra-portal']/div//section[@role='alertdialog']/footer/button[2]",
        ).click()
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
