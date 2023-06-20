import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import baseLogin
from selenium.webdriver.common.keys import Keys


class TestPelanggan(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_pelanggan(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("lala")  # isi nama
        driver.find_element(By.ID, "no.hp").send_keys("08111111111")  # isi no.hp
        driver.find_element(By.ID, "alamat").send_keys("jl. abc no 1")  # isi alamat
        driver.find_element(By.ID, "keterangan").send_keys(
            "tidak ada keterangan"
        )  # isi keterangan
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        response_data = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//table[@role='table']/tbody/tr[1]/td[1]",
        ).text
        self.assertIn("lala", response_data)

    def test_a_success_add_pelanggan_nohp_invalid(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("lala")  # isi nama
        driver.find_element(By.ID, "no.hp").send_keys("+628111111111")  # isi no.hp
        driver.find_element(By.ID, "alamat").send_keys("jl. abc no 1")  # isi alamat
        driver.find_element(By.ID, "keterangan").send_keys(
            "tidak ada keterangan"
        )  # isi keterangan
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        time.sleep(1)
        response_data = driver.find_element(By.ID, "chakra-alert").text
        self.assertIn('"phone" must be a number', response_data)

    def test_a_success_edit_pelanggan(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[4]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[4]//div[@role='menu']/a[@role='menuitem']",
        ).click()  # ubah button
        time.sleep(1)
        # Menghapus teks yang ada menggunakan kombinasi tombol keyboard
        inputKeterangan = driver.find_element(By.ID, "keterangan")
        inputKeterangan.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputKeterangan.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        inputKeterangan.send_keys("keterangan")  # ubah teks jadi keterangan
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def test_a_success_delete_pelanggan(self):
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/customers"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[4]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[4]//div[@role='menu']/button[@role='menuitem']",
        ).click()  # delete button
        time.sleep(2)
        driver.find_element(
            By.CLASS_NAME,
            "css-n45e6f",
        ).click()  # confirm delete button
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
