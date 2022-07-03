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

    paisOrigen = "SJO"
    paisDestino = "ADZ"
    fechaIni = "2022-07-14"
    fechaFin = "2022-07-21"
    urlPrincipal = "https://www.kayak.com/flights/"+paisOrigen+"-"+paisDestino+"/"+fechaIni+"/"+fechaFin+"?sort=bestflight_a"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
        driver = cls.driver
        driver.implicitly_wait(10)
        

   
    # Buscar vuelos entre 2 destinos Seleccionados (Costa Rica - San Andres)
    def test_casoautomatico1(self):
        driver = self.driver    
        
        # Test name: Caso automatico 1
        # Step # | name | target | value
        # 1 | open | https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a | 
        driver.get(urlPrincipal)
        # 2 | setWindowSize | 1696x1026 | 
        driver.set_window_size(1696, 1026)
        # 3 | click | css=.yWJT-insideDrawer path | 
        driver.find_element(By.CSS_SELECTOR, ".yWJT-insideDrawer path").click()
        # 4 | click | linkText=Flights | 
        driver.find_element(By.LINK_TEXT, "Flights").click()
        # 5 | click | css=.c8LPF-icon | 
        driver.find_element(By.CSS_SELECTOR, ".c8LPF-icon").click() 

    # Buscar las restricciones de un pais seleccionado (Costa Rica)
    def test_casoautomatico2(self):
        driver = self.driver 

        # Test name: Caso automatico 2
        # Step # | name | target | value
        # 1 | open | https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a | 
        driver.get(urlPrincipal)
        # 2 | setWindowSize | 1552x840 | 
        driver.set_window_size(1552, 840)
        # 3 | click | css=.yWJT-insideDrawer .svg-image | 
        driver.find_element(By.CSS_SELECTOR, ".yWJT-insideDrawer .svg-image").click()
        # 4 | click | css=.UVLb:nth-child(2) > .hsCY:nth-child(3) > .hsCY-menu-item-title | 
        driver.find_element(By.CSS_SELECTOR, ".UVLb:nth-child(2) > .hsCY:nth-child(3) > .hsCY-menu-item-title").click()
        # 5 | click | css=.Gt8D-mod-padding-default:nth-child(1) | 
        driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div/div[2]/div/div/div/div").click()
        # 6 | click | css=.Gt8D:nth-child(1) .c3I-P-name | 
        driver.find_element(By.XPATH, "//span[contains(.,'Costa Rica')]").click() 
        
    # Buscar un paquete entre 2 destinos seleccionados (Costa Rica - Las Vegas)
    def test_casoautomatico3(self):
        driver = self.driver 

        # Test name: Caso automatico 3
        # Step # | name | target | value
        # 1 | open | https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a | 
        driver.get(urlPrincipal)
        # 2 | setWindowSize | 1552x840 | 
        driver.set_window_size(1552, 840)
        # 3 | click | css=.yWJT-insideDrawer path | 
        driver.find_element(By.CSS_SELECTOR, ".yWJT-insideDrawer path").click()
        # 4 | click | css=.hsCY:nth-child(5) > .hsCY-menu-item-title | 
        driver.find_element(By.CSS_SELECTOR, ".hsCY:nth-child(5) > .hsCY-menu-item-title").click()
        # 5 | runScript | window.scrollTo(0,1870.4000244140625) | 
        driver.execute_script("window.scrollTo(0,1870.4000244140625)")
        # 6 | click | linkText=Las Vegas Vacations | 
        driver.find_element(By.LINK_TEXT, "Las Vegas Vacations").click()
        # 7 | click | css=#S-95-submit > .v-c-p | 
        #driver.find_element(By.CSS_SELECTOR, "#S-95-submit > .v-c-p").click() 

    
    # Buscar opciones de cosas para hacer en un destino seleccionado (San Andres)
    def test_casoautomatico4(self):
        driver = self.driver 

        # Test name: Caso automatico 4
        # Step # | name | target | value
        # 1 | open | https://www.kayak.com/flights/SJO-ADZ/2022-07-14/2022-07-21?sort=bestflight_a | 
        driver.get(urlPrincipal)
        # 2 | setWindowSize | 1552x840 | 
        driver.set_window_size(1552, 840)
        # 5 | click | css=.yWJT-insideDrawer .svg-image | 
        driver.find_element(By.CSS_SELECTOR, ".yWJT-insideDrawer .svg-image").click()
        # 6 | click | css=.hsCY:nth-child(4) > .hsCY-menu-item-title | 
        driver.find_element(By.CSS_SELECTOR, ".hsCY:nth-child(4) > .hsCY-menu-item-title").click()
        # 7 | click | linkText=See all | 
        driver.find_element(By.LINK_TEXT, "See all").click()
        # 8 | runScript | window.scrollTo(0,0) | 
        driver.execute_script("window.scrollTo(0,0)")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    


if __name__ == '__main__':
    paisOrigen = "SJO"
    paisDestino = "ADZ"
    fechaIni = "2022-07-14"
    fechaFin = "2022-07-21"
    urlPrincipal = "https://www.kayak.com/flights/"+paisOrigen+"-"+paisDestino+"/"+fechaIni+"/"+fechaFin+"?sort=bestflight_a"

    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='Reporte de prueba'))