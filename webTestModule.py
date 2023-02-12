from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class WebModule:
    def __init__(self,initPage:str = "https://www.104.com.tw/jobs/main/"):
        self.driverPath="chromedriver.exe"
        self.initWebdriver(initPage)

    def initWebdriver(self,initPage:str):
        self.service = Service(self.driverPath)
        self.service.start()
        capabilities = {'acceptInsecureCerts': True}
        self.driver = webdriver.Remote(self.service.service_url,capabilities)
        self.driver.implicitly_wait(5)
        self.driver.get(initPage)

    def close(self):
        self.driver.quit()