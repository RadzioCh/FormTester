from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
import pprint
import sys
from Models.LLMAssistant import LLMAssistant
import time

class FillForm:

    # {'Tag': 'input', 'Type': 'checkbox', 'Name': 'form[consents_toSave10]', 'Value': '1', 'Label': 'Brak etykiety'}

    def __init__(self, form_field_map, llm_conversation):
        self.form_field_map = form_field_map
        self._url = form_field_map['url']
        self.llm_conversation = llm_conversation

    def fill(self, form_data):

        # pprint.pprint(self.form_field_map)
        # sys.exit()
        
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self._url)

        iter = 1
        for field in form_data:
            print(field['Tag'])
            
            match field['Tag']:
                case 'input':
                    match field['Type']:
                        case 'text':
                            # time.sleep(2)
                            response_mistral =self.llm_conversation.ask_simple_question("<field_elements>"+str(field)+"</field_elements>")

                            file_input = driver.find_element(By.NAME, field['Name'])
                            file_input.send_keys(response_mistral.content)
                        case 'checkbox':
                            # time.sleep(2)
                            pprint.pprint(field)
                            response_mistral =self.llm_conversation.ask_simple_question("<field_elements>"+str(field)+"</field_elements>")
                            checkbox_field = driver.find_element(By.NAME, field['Name'])
                            if response_mistral.content == 1:
                                checkbox_field.click()

                        
                case 'select':
                    wynik = "Dwa"
                
                case _:
                    wynik = f"Pole "+field['Tag']+" => typ "+field['Type']+" nie obsługiwane"
            
            if(iter == 12):
                print('################ SLEEP #################')
                time.sleep(20)
                iter = 0
            
            iter += 1
            

            
            

       # driver.quit()  # Zamknij przeglądarkę   