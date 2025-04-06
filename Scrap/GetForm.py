from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from langchain.chat_models import ChatMistralAI  # Nowe API Mistral Large
from langchain.chains import RetrievalQA


class GetForm():

    def __init__(self):
        self._url = 'https://dev.wnioskomat.com/embed/form?typ=aasa_standard_connect&source=wnioskomat.com&origin_url=https%3A%2F%2Fdev.wnioskomat.com%2Fwniosek'
    
    def init(self):
        form_data = self.get_form_by_selenium()
        print(form_data)
        

    def get_form_by_requests(self):
        response = requests.get(self._url)
        soup = BeautifulSoup(response.text, "html.parser")

        form = soup.find("form")
        print(form)
        
    def get_form_by_selenium(self):
        

        # Konfiguracja Selenium (Chrome)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self._url)

        driver.implicitly_wait(3) # Czekaj na załadowanie elementu (np. 10 sekund)

        # Pobierz dane (np. listę produktów)
        forms = driver.find_elements(By.TAG_NAME, "form")
        form_data = []

        if forms:
            form = forms[0]  # Bierzemy pierwszy formularz

            # Pobierz wszystkie etykiety i ich powiązania
            labels = form.find_elements(By.TAG_NAME, "label")
            label_map = {}
            for label in labels:
                try:
                    label_for = label.get_attribute("for")
                    label_map[label_for] = label.text
                except:
                    pass

            print("\nInformacje o polach formularza:")
            # Znajdź wszystkie pola formularza wewnątrz formularza
            form_fields = form.find_elements(By.XPATH, ".//input | .//select | .//textarea")

            for field in form_fields:
                field_info = self.print_field_info(field, label_map)
                form_data.append(field_info)

        else:
            print("Nie znaleziono żadnego formularza na stronie.")

        driver.quit()  # Zamknij przeglądarkę
        return form_data
        


    def print_field_info(self, field: WebElement, label_map: dict):
        """Wyświetla informacje o polu formularza wraz z powiązaną etykietą."""
        try:
            field_type = field.get_attribute("type")
        except:
            field_type = "None"
        try:
            field_name = field.get_attribute("name")
        except:
            field_name = "None"
        try:
            field_value = field.get_attribute("value")
        except:
            field_value = "None"
        try:
            field_tag_name = field.tag_name
        except:
            field_tag_name = "None"
        try:
            field_id = field.get_attribute("id")
        except:
            field_id = "None"

        label_text = "Brak etykiety"
        if field_id in label_map:
            label_text = label_map[field_id]
        else:
            excluded_types = ('checkbox', 'radio', 'file', 'submit', 'reset', 'button', 'hidden')
            if field_type not in excluded_types:
                try:
                    # Sprawdza czy etykieta jest przed polem.
                    label_element = field.find_element(By.XPATH, "./preceding-sibling::label")
                    label_text = label_element.text
                except NoSuchElementException:
                        pass

        return {
            "Tag": field_tag_name,
            "Type": field_type,
            "Name": field_name,
            "Value": field_value,
            "Label": label_text
        }

    