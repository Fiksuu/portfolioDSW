import re

def sprawdz_email(email):
    wzorzec = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(wzorzec, email):
        return True
    return False

def wczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            adresy_email = plik.readlines()
    except FileNotFoundError:
        print("Plik nie istnieje.")
        return []
    except Exception as e:
        print(f"Wystąpił błąd podczas odczytu pliku: {str(e)}")
        return []
    
    return [email.strip() for email in adresy_email]

def sprawdz_plik(nazwa_pliku):
    adresy_email = wczytaj_plik(nazwa_pliku)
    for email in adresy_email:
        if sprawdz_email(email):
            print(f"Adres email {email} jest poprawny.")
        else:
            print(f"Adres email {email} jest niepoprawny.")

nazwa_pliku = 'adresyemail.txt'
sprawdz_plik(nazwa_pliku)
