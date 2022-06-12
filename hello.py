from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_hello_world(self):
        driver = self.driver
        driver.get("http://www.ebay.com")

    def test_visit_wiki(self):
        driver = self.driver
        driver.get("https://www.wikipedia.org")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world'))