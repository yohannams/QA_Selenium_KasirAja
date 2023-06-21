import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import baseLogin
from selenium.webdriver.common.keys import Keys


class TestPenjualan(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_failed_search(self):  # TC22
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        element = driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-d4ejuc']/div[1]/div[@class='chakra-input__group css-4302v8']/input[@value='2023-5-21']",
        )
        is_disabled = element.is_enabled()
        self.assertFalse(is_disabled)

    def test_a_success_add_penjualan(self):  # TC23
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()
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
            "2"
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-rltemf']/input",
        ).send_keys(
            "100000"
        )  # isi jumlah bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        time.sleep(1)
        driver.find_element(
            By.CLASS_NAME,
            "chakra-modal__content-container",
        )
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']//button[@type='button']",
        ).click()  # tutup

    def test_a_success_add_penjualan_empty_jumlah_bayar(self):  # TC24
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()
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
            "2"
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']/div[@class='chakra-portal']/div//section[@role='alertdialog']/footer/button[2]",
        ).click()  # ya
        time.sleep(1)
        driver.find_element(
            By.CLASS_NAME,
            "chakra-modal__content-container",
        )
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']//button[@type='button']",
        ).click()  # tutup

    def test_a_success_add_penjualan_invalid_jumlah_barang(self):  # TC25
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[4]/td[1]",
        ).click()
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
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']/div[@class='chakra-portal']/div//section[@role='alertdialog']/footer/button[2]",
        ).click()  # ya
        time.sleep(1)
        driver.find_element(
            By.CLASS_NAME,
            "chakra-modal__content-container",
        )
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']//button[@type='button']",
        ).click()  # tutup
        id_pattern = r"toast-\d+-title"
        driver.find_element(
            By.XPATH,
            f"//*[matches(@id, '{id_pattern}')]",
        )

    def test_a_success_add_penjualan_invalid_jumlah_barang_kurang_dari_stok(
        self,
    ):  # TC26
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[4]/td[1]",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']/div[@class='chakra-portal']/div//section[@role='alertdialog']/footer/button[2]",
        ).click()  # ya
        time.sleep(1)
        response_data = driver.find_element(
            By.CLASS_NAME,
            "chakra-alert__desc",
        ).text
        self.assertIn("transaksi gagal: stock tidak cukup", response_data)

    def test_a_success_add_penjualan_diskon_valid(
        self,
    ):  # TC27
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # klik tombol produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
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
            "2"
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.ID,
            "diskon",
        ).send_keys("10")
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-rltemf']/input",
        ).send_keys(
            "100000"
        )  # isi jumlah bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait
        driver.find_element(
            By.XPATH,
            "/html/body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']//button[@type='button']",
        ).click()  # tutup

    def test_a_success_add_penjualan_invalid_diskon(
        self,
    ):  # TC28
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # klik tombol produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
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
            "2"
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.ID,
            "diskon",
        ).send_keys("1000000")
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-rltemf']/input",
        ).send_keys(
            "100000"
        )  # isi jumlah bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

        response_data = driver.find_element(
            By.CLASS_NAME,
            "chakra-alert__title",
        ).text
        self.assertIn("error", response_data)

    def test_a_failed_add_penjualan(self):  # TC29
        # steps
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-1xhj18k']/button[@type='button']",
        ).click()  # pilih produk
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "//body[@class='chakra-ui-light']//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()
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
            "2"
        )  # isi jumlah brg
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-rltemf']/input",
        ).send_keys(
            "10"
        )  # isi jumlah bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        time.sleep(1)
        driver.find_element(By.ID, "chakra-alert")

    def test_a_failed_add_penjualan_produk_kosong(
        self,
    ):  # TC30
        driver = self.browser  # buka web browser
        baseLogin.test_a_success_login(driver)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'a[href="/sales"]').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div//div[@class='css-1t33j5j']/a[@href='/sales/create']",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.ID,
            "pelanggan",
        ).click()  # pelanggan
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@class='chakra-modal__content-container css-v9b9hc']/section[@role='dialog']/div[@class='chakra-modal__body css-qlig70']/table[@role='table']/tbody/tr[1]/td[1]",
        ).click()  # pilih pelanggan
        time.sleep(1)
        driver.find_element(
            By.ID,
            "diskon",
        ).send_keys("100")
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']//div[@class='css-rltemf']/input",
        ).send_keys(
            "10000"
        )  # isi jumlah bayar
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html//div[@id='root']/div/div[@class='css-k008qs']/div[@class='css-1r35f0l']//div[@class='css-n4rzf0']/button[@type='button']",
        ).click()  # tombol bayar
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "chakra-alert__title"))
        )  # eksplisit wait

        response_data = driver.find_element(
            By.CLASS_NAME,
            "chakra-alert__title",
        ).text
        self.assertIn("error", response_data)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
