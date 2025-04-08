from Scrap.GetForm import GetForm
from Models.Mistral import Mistral
import yaml
import sys
from Yml.ConfigParse import ConfigParse
import os
import pprint



class Fire:
    def __init__(self):
        self.mistral_conversation = Mistral()
    
    def init(self):
        
        config_parse = ConfigParse()
        form_config_map = config_parse.parse()

        pprint.pprint(form_config_map)

        sys.exit()

        # TO DO: zapisywanie plików na dysku cza zrobić w GetForm

        if form_config_map['saveed_form_map']['use_if_exist'] == True and form_config_map['saveed_form_map']['files'] != []:
            for file in form_config_map['saveed_form_map']['files']:
                path_to_file = 'SavedForms/'+form_config_map['name']+'/'+file
                print(path_to_file)
                if os.path.exists(path_to_file):
                    print('jest plik zapisany')
                else:
                    print('PLIK '+path_to_file+' NIE ISTNIEJE, PRZERYWAM TEST')
                    sys.exit()
            
        else:
            get_form = GetForm(self.mistral_conversation, form_config_map)
            form_map = get_form.init()
            print(form_map)
        


####################################
fire = Fire()
fire.init()
