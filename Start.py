from Scrap.GetForm import GetForm
from Models.Mistral import Mistral
import yaml
import sys
from Yml.ConfigParse import ConfigParse
import os
import pprint
import json
from FillForm.FillForm import FillForm


class Fire:
    def __init__(self):
        config_parse = ConfigParse()
        form_config_map = config_parse.parse()
        self.form_config_map = form_config_map

        self.mistral_conversation = Mistral()
        self.fill_form = FillForm(self.form_config_map)
    
    def init(self):
        get_form_start = 1
        

        # TO DO: zapisywanie plików na dysku cza zrobić w GetForm

        if self.form_config_map['saved_form_map']['use_if_exist'] == True and self.form_config_map['saved_form_map']['files'] != []:
            get_form_start = 0
            for file in self.form_config_map['saved_form_map']['files']:
                path_to_file = 'SavedForms/'+self.form_config_map['name']+'/'+file
                # print(path_to_file)
                if os.path.exists(path_to_file):
                    with open(path_to_file, 'r', encoding='utf-8') as ptf:
                        form_data = json.load(ptf)
                        
                        self.fill_form.fill_form(form_data)
                        # pprint.pprint(form_data)
                        # sys.exit()

                else:
                    print('PLIK '+path_to_file+' NIE ISTNIEJE, URUCHAMIAM POBIERANIE DANYCH FORMULARZA')
                    get_form_start = 1
            
        if get_form_start == 1:
            which_shot = 1
            while True:
                
                get_form = GetForm(self.mistral_conversation, self.form_config_map, which_shot)
                form_map = get_form.init()
                which_shot += 1
                
        


####################################
fire = Fire()
fire.init()
