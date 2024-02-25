import re

try:
    with open('P2ĆW2_Błędy_i_Wyjątki/3/adresyemail.txt', 'r') as f:
        lines = f.readlines()
    pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    for line in lines:
        if pattern.fullmatch(line.strip()):
            print(f'Adres e-mail {line.strip()} jest poprawny.')
        else:
            print(f'Adres e-mail {line.strip()} jest niepoprawny.')
except FileNotFoundError:
    print('Plik nie istnieje.')
except Exception as e:
    print(f'Wystąpił błąd: {e}')
