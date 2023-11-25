from config import DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import chromedriver_autoinstaller_fix

def get_driver():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    options.add_experimental_option("prefs",prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
    options.add_experimental_option("useAutomationExtension", False)
    #This is mentioned in documentation it is a must add item to prevent bugs
    options.add_argument("--disable-gpu")
    service=ChromeService(executable_path=DRIVER_PATH)
    chromedriver_autoinstaller_fix.install()
    driver=webdriver.Chrome(service=service,options=options)
    return driver