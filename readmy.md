** Pakiety **

    ## python -m venv venv -> Co to jest venv? To osobne środowisko Pythona w folderze twojego projektu. Trzyma własne pakiety — nie miesza się z globalnym Pythonem. 

                                Chroni projekt przed konfliktem wersji bibliotek.


    Znajdują się w pliku  requirements.txt

    1. Instalacja
        - pip install -r requirements.txt
        To polecenie zainstaluje wszystkie pakiety wymienione w pliku requirements.txt wraz z ich określonymi wersjami jeśli już są pakiety to zainstaluje tylko te których nie ma

    2. Aktualizacja pliku requirements.txt
        - pip freeze > requirements.txt
