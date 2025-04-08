import yaml

class ConfigParse:
    def __init__(self):
        pass
        
    def parse(self):
        with open('config.yml', 'r') as f:
            dane_yml = yaml.safe_load(f)

        form_config_map = {}
        for dane_var in dane_yml['forms']:
            if dane_yml['forms'][dane_var]['active'] == True:
                form_config_map = dane_yml['forms'][dane_var]
                break

        return form_config_map