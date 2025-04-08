import sys
from Models.Mistral import Mistral
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

class FormTest:
    def __init__(self, form_field_map):
        self.form_field_map = form_field_map
        self.mistral_conversation = Mistral()
        
    def init(self):
        self.form_test()
        

    def form_test(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.form_field_map['url'])

        driver.implicitly_wait(1) # Czekaj na załadowanie elementu (np. 10 sekund)

        # Pobierz dane (np. listę produktów)
        forms = driver.find_elements(By.TAG_NAME, "form")
