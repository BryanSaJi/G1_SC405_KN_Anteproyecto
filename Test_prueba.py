from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class TestPrueba(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)


    def test_TestPrueba(self):
        driver = self.driver
        driver.get("https://www.es.kayak.com/")
        wait(2000)

    def test_visit(self):
        driver = self.driver
        driver.get("https://www.es.kayak.com/stays")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='Reporte de prueba'))