from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class TestPrueba(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)

   

    def test_casoautomatico1(self):
        driver = self.driver    
        
        # Test name: Caso automatico 1
        # Step # | name | target | value
        # 1 | open | https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a | 
        driver.get("https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a")
        # 2 | setWindowSize | 1696x1026 | 
        driver.set_window_size(1696, 1026)
        # 3 | click | css=.yWJT-insideDrawer path | 
        driver.find_element(By.CSS_SELECTOR, ".yWJT-insideDrawer path").click()
        # 4 | click | linkText=Flights | 
        driver.find_element(By.LINK_TEXT, "Flights").click()
        # 5 | click | css=.c8LPF-icon | 
        driver.find_element(By.CSS_SELECTOR, ".c8LPF-icon").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='Reporte de prueba'))