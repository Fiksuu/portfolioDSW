from datetime import datetime

try:
    date_string = input('Podaj datę i czas w formacie rok-miesiąc-dzień godzina:minuta:sekunda: ')
    date_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    print(f'Data i czas to: {date_object}')
except ValueError:
    print('Nieprawidłowy format daty i czasu.')
except Exception as e:
    print(f'Wystąpił błąd: {e}')
