import os
import unittest
from appium import webdriver
from time import sleep
 
class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = '11019d33a982924a'
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'Chess Free.apk'))
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        #self.driver.quit()

        # find all id/ all names
        #ids = self.driver.find_elements_by_xpath('//*[@id]')
        #sa = self.driver.find_elements_by_name('//*')
 
    def test_single_player_mode(self):
        "Test the Single Player mode launches correctly"
        element = self.driver.find_element_by_name("Accept")
        element.click()
        #self.driver.find_element_by_name("Single Player").click()
        #textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        #self.assertEqual('MATCH SETTINGS', textfields[0].text)
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
