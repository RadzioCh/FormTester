from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement

class FillForm:

    def __init__(self, form_field_map):
        self.form_field_map = form_field_map

    def fill(self, form_data):
        
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver.get(self._url)

        for field in form_data:
            
            print(field)
            

        # driver.quit()  # Zamknij przeglądarkę   