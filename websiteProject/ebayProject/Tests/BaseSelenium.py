import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class baseSelenium():

    def selenium_start(self, url):
        print("Test initialized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        return driver

    def selenium_end(self, driver):
        driver.close()
        print("Test concluded")