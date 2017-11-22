# encoding: utf-8

"""
帶入單元測試的函式庫
可讓執行程式時同時執行函式庫內的單元測試內容
這範例是個完整unittest testcase framework
從定義class開始
之後個別定義函式 setUp(), test_testcase(), tearDown()
setUp 是為測試準備環境
tearDown 用來清理環境
testcase的函式命名必須用"test_"開頭
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase): #命名class, 此class繼承了unittest.Testcase, 那這class 便是一個testcase

    def setUp(self): #為測試準備環境。
        self.driver = webdriver.Firefox()

    def test_search_in_python_org1(self): #在class裡面看到"test_" 開頭的函式, loader則會判別為這是此class裡面的testcase
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn('Python', driver.title)

    def test_search_in_python_org2(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No result found' not in driver.page_source

    def test_search_in_python_org3(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No result found' in driver.page_source

    def tearDown(self): #清理測試環境
        self.driver.quit()

if __name__ == "__main__": #判別是否為被import的狀態
    unittest.main() #最基本的執行testcase方法