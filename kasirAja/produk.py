import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import baseLogin
from selenium.webdriver.common.keys import Keys


class TestProduk(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_produk(self):  # TC13
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("beras")  # isi nama
        driver.find_element(By.ID, "deskripsi").send_keys(
            "beras merah"
        )  # isi deskripsi
        driver.find_element(By.ID, "harga beli").send_keys("60000")  # isi harga beli
        driver.find_element(By.ID, "harga jual").send_keys("70000")  # isi harga jual
        driver.find_element(By.ID, "stok").send_keys("10")  # isi stok
        driver.find_element(By.ID, "kategori").click()
        driver.find_element(
            By.XPATH,
            "/html//section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[@role='gridcell']",
        ).click()  # pilih kategori
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        response_data = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//table[@role='table']/tbody/tr[1]/td[2]",
        ).text
        self.assertIn("beras", response_data)

    def test_a_success_add_produk_empty_deskripsi(self):  # TC14
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products/create"]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("beras coklat")  # isi nama
        driver.find_element(By.ID, "harga beli").send_keys("60000")  # isi harga beli
        driver.find_element(By.ID, "harga jual").send_keys("70000")  # isi harga jual
        driver.find_element(By.ID, "stok").send_keys("10")  # isi stok
        driver.find_element(By.ID, "kategori").click()
        driver.find_element(
            By.XPATH,
            "/html//section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[@role='gridcell']",
        ).click()  # pilih kategori
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        response_data = driver.find_element(
            By.CLASS_NAME,
            "chakra-alert",
        )
        self.assertIn(response_data)

    def test_a_success_edit_produk(self):  # TC15
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]//div[@role='menu']/a[@role='menuitem']",
        ).click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys(" muda")  # isi nama
        driver.find_element(By.ID, "stok").send_keys("0")  # isi stok
        driver.find_element(By.ID, "kategori").click()
        driver.find_element(
            By.XPATH,
            "/html//section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[3]/td[@role='gridcell']",
        ).click()  # pilih kategori
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def test_a_success_edit_produk_duplikasi_kode(self):  # TC16
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]//div[@role='menu']/a[@role='menuitem']",
        ).click()
        time.sleep(1)
        inputKode = driver.find_element(By.ID, "kode")
        inputKode.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputKode.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        # driver.find_element(By.ID, "kode").clear()  # ubah kode
        time.sleep(1)
        inputKode.send_keys("1")  # ubah kode
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        time.sleep(1)
        driver.find_element(By.ID, "chakra-alert")

    def test_a_failed_edit_hargajual_invalid(self):  # TC17
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]//div[@role='menu']/a[@role='menuitem']",
        ).click()
        time.sleep(1)
        inputHarga = driver.find_element(By.ID, "harga jual")
        inputHarga.send_keys(Keys.CONTROL + "a")  # Memilih seluruh teks
        inputHarga.send_keys(Keys.DELETE)  # Menghapus teks yang terpilih
        # driver.find_element(By.ID, "kode").clear()  # ubah kode
        time.sleep(1)
        inputHarga.send_keys("5500")  # ubah kode
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()  # simpan
        time.sleep(1)
        driver.find_element(By.ID, "chakra-alert")

    def test_a_success_delete_produk(self):  # TC18
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]/button[@type='button']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']//table[@role='table']/tbody/tr[1]/td[10]//div[@role='menu']/button[@role='menuitem']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']/div[@class='chakra-portal']/div//section[@role='alertdialog']/footer/button[2]",
        ).click()
        time.sleep(1)
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
