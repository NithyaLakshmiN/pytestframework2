
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readproperties import ReadConfig
#from utilities.customLogger import LogGen
from icecream import ic



class Test_Login_001:
    baseURL = ReadConfig.getapplicationurl()
    #username = ReadConfig.getusername()
    #password = ReadConfig.getpassword()
    #logger = LogGen.loggen()


    def test_homepagetitle(self, setup):
        print("*************** Test_001_Login *****************")
        #self.logger.info("****Started Home page title test ****")
        self.driver = setup
        #self.driver = webdriver.Firefox()
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        print(actual_title)

        if actual_title == "NovaGuide View":
            print("**** Home page title test passed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            assert True
        else:
            print("**** Home page title test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            assert False


