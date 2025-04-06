from Scrap.GetForm import GetForm
from Models.Mistral import Mistral

class Fire:
    def __init__(self):
        self.mistral_conversation = Mistral()
    
    def init(self):

        get_form = GetForm(self.mistral_conversation)
        get_form.init()
    



####################################
fire = Fire()
fire.init()