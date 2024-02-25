from datetime import datetime

def wczytaj_date():
    while True:
        data_wejsciowa = input("Podaj datę i czas w formacie 'rok-miesiąc-dzień godzina:minuta:sekunda': ")
        try:
            data = datetime.strptime(data_wejsciowa, '%Y-%m-%d %H:%M:%S')
            return data
        except ValueError:
            print("Nieprawidłowy format daty lub czasu. Spróbuj ponownie.")

data = wczytaj_date()
print(f"Wczytana data i czas to: {data}")
