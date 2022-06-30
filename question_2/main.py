
import unittest
import element as el
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def execute_1_to_9_process(driver, timeout=5):
    '''
    點擊 1 加到 9 的過程
    '''
    ele_list = [el.id_1_btn, el.id_2_btn, el.id_3_btn, el.id_4_btn, el.id_5_btn, el.id_6_btn, el.id_7_btn, el.id_8_btn, el.id_9_btn]
    for i in ele_list:
        get_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, i)),message='無發現 {0}'.format(i))
        get_ele.click()
        get_add_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, el.id_add_btn)),message='無發現 {0}'.format(el.id_add_btn))
        get_add_ele.click()

def excute_add_10_process(driver, timeout=5):
    '''
    點擊 1, 0, = 元素 
    '''
    get_1_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, el.id_1_btn)),message='無發現 {0}'.format(el.id_1_btn))
    get_1_ele.click()
    get_0_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, el.id_0_btn)),message='無發現 {0}'.format(el.id_0_btn))
    get_0_ele.click()
    get_eq_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, el.id_eq_btn)),message='無發現 {0}'.format(el.id_eq_btn))
    get_eq_ele.click()
    
def get_result_number(driver, timeout=5):
    '''
    取得加總結果
    '''
    get_result_ele = WebDriverWait(driver, timeout=timeout).until(EC.visibility_of_element_located((By.ID, el.id_result_text)),message='無發現 {0}'.format(el.id_result_text))
    get_result_number = get_result_ele.get_attribute('text')
    return get_result_number

class ComputerAndroidTests(unittest.TestCase):
    
    
    def setUp(self):
        desired_caps = {}  # 空字典 需要給予測試手機相關資訊
        desired_caps['platformName'] = 'Android'  # 測試的平台
        desired_caps['platformVersion'] = '10.0'  # 手機os版本
        desired_caps['deviceName'] = 'Pixel XL'  # 看你手機的名稱是什麼
        desired_caps['automationName'] = "UiAutomator2"  # 一定要的！
        desired_caps['udid'] = "HT6520200107"  # device id
        desired_caps['appPackage'] = 'com.google.android.calculator'
        desired_caps['appActivity'] = 'com.android.calculator2.Calculator'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        
    def tearDown(self):
        self.driver.quit()
        
    def test_add_case(self):
        execute_1_to_9_process(driver=self.driver)
        excute_add_10_process(driver=self.driver)
        get_add_result = get_result_number(driver=self.driver)
        self.assertEqual(get_add_result, '55', msg='計算的結果有錯誤，不符合預期')
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComputerAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
