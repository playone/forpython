# encoding: utf-8

"""
帶入單元測試的函式庫
可讓執行程式時同時執行函式庫內的單元測試內容
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pyccon')
        elem.send_keys(Keys.RETURN)
        assert 'No result found' not in driver.page_source


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()