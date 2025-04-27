from Mistral import Mistral
import time

mistral_conversation = Mistral()

response_mistral = mistral_conversation.ask_simple_question("Cześć, jak się masz?")
print(response_mistral.content)

time.sleep(2)
response_mistral = mistral_conversation.ask_simple_question("O co zapytałem przed chwilą?")
print(response_mistral.content)

time.sleep(2)
response_mistral = mistral_conversation.ask_simple_question("Kto to jest, mój ojciec ma syna i to nie jestem ja?")
print(response_mistral.content)

print('...oo.............ooooooooo')
print(mistral_conversation.get_history_as_text("default"))