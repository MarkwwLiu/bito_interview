from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time


def move_to_bottom(driver):
    """
    移動到網頁最下方
    Args:
        driver: 給予driver參數值
    """
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
        
def verify_search_results(get_verify_list, get_verify_str):
    """
    判斷list中是否有相關的str，有回傳True, 無則回傳 False
    Args:
        get_verify_list (list): 給予需要判斷的 list
        get_verify_str (str): 給予要判斷的 str

    Returns:
        bool: 有回傳True, 無回傳False
    """
   
    for verify in get_verify_list:
        if get_verify_str in str(verify):
            return True
    return False

class GoogleSearchBitoProTestCase(unittest.TestCase):
    
    def setUp(self):
        """
        安裝最新版本的ChromeDriver，叫起Chrome瀏覽器
        指定給 self.driver
        """
        self.search_key = 'BitoPro'
        self.web_url = 'https://www.google.com/'
        self.search_title_list = []
        self.search_title_url_list = []
        self.verify_title_str = 'BitoPro 台灣幣託交易所'
        self.verify_url_str = 'https://www.bitopro.com'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.set_page_load_timeout(15)

    def tearDown(self):
        """
        關閉 Chrome 瀏覽器
        """
        self.driver.close()
        
    def test_verify_search_title_results(self):
        '''
        搜尋結果頁面中資料是否顯示 BitoPro 台灣幣託交易所 相關網頁標題
        搜尋結果頁面中資料是否顯示 https://www.bitopro.com 相關網頁連結
        '''
        self.driver.get(self.web_url)
        get_search_ele = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.NAME, 'q')),message='無發現 {0}'.format('q'))
        get_search_ele.send_keys(self.search_key)
        get_search_ele.send_keys(Keys.RETURN)

        move_to_bottom(driver=self.driver)

        get_search_title_eles = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div a h3')),message='無發現 {0}'.format('div a h3'))
        for search_title in get_search_title_eles:
            self.search_title_list.append(search_title.text)
        
        get_search_title_url_eles = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div a cite')),message='無發現 {0}'.format('div a cite'))
        for search_title_url in get_search_title_url_eles:
            self.search_title_url_list.append(search_title_url.text)
        
        is_verify_search_title = verify_search_results(get_verify_list=self.search_title_list, get_verify_str=self.verify_title_str)
        is_verify_search_url = verify_search_results(get_verify_list=self.search_title_url_list, get_verify_str=self.verify_url_str)
        
        self.assertTrue(is_verify_search_title, msg='無搜尋到相關 {0} 標題'.format(self.verify_title_str))
        self.assertTrue(is_verify_search_url, msg='無搜尋到相關 {0} 連結'.format(self.verify_url_str))

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchBitoProTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)