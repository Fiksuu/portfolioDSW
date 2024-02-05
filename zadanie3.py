import os
import datetime
import requests
import json

class Invoice:
    def __init__(self, amount, currency, issue_date):
        self.amount = amount
        self.currency = currency
        self.issue_date = issue_date
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def calculate_total_payment(self):
        total_payment = 0
        for payment in self.payments:
            payment_rate = get_exchange_rate(payment.currency, payment.payment_date)
            total_payment += payment.amount / payment_rate
        return total_payment

class Payment:
    def __init__(self, amount, currency, payment_date):
        self.amount = amount
        self.currency = currency
        self.payment_date = payment_date

def get_exchange_rate(currency, date):
    attempts = 0
    while attempts < 10:
        try:
            response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date}/')
            data = json.loads(response.text)
            return data['rates'][0]['mid']
        except:
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            date -= datetime.timedelta(days=1)
            date = date.strftime("%Y-%m-%d")
            attempts += 1
    print(f"Nie udało się pobrać kursu waluty {currency} dla daty {date}.")
    return None

def calculate_difference(invoice, payment):
    invoice_rate = get_exchange_rate(invoice.currency, invoice.issue_date)
    payment_rate = get_exchange_rate(payment.currency, payment.payment_date)

    if invoice_rate and payment_rate:
        return (payment.amount/payment_rate) - (invoice.amount/invoice_rate)
    else:
        return None

def save_to_file(filename, data):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print(f'Wystąpił błąd podczas zapisywania do pliku: {e}')

def load_invoices_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f'Plik {filename} jest niepoprawnie skonfigurowany. Sprawdź, czy jest poprawnym plikiem JSON.')
        return []
    except Exception as e:
        print(f'Wystąpił błąd podczas wczytywania danych z pliku: {e}')
        return []

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_amount(amount_text):
    try:
        amount = float(amount_text)
        if amount <= 0:
            return False
        return True
    except ValueError:
        return False

def main():
    if os.path.exists("output.txt"):
        delete_file = input("Plik output.txt istnieje. Czy chcesz go usunąć? (tak/nie): ")
        if delete_file.lower() == "tak":
            os.remove("output.txt")

    mode = input("Wybierz tryb (wsadowy/manualny): ")

    if mode.lower() == "wsadowy":
        filename = input("Podaj nazwę pliku z danymi: ")
        invoices_data = load_invoices_from_file(filename)
    elif mode.lower() == "manualny":
        invoices_data = []
        while True:
            while True:
                amount_text = input("Podaj kwotę faktury: ")
                if validate_amount(amount_text):
                    amount = float(amount_text)
                    break
                else:
                    print("Błędna kwota. Spróbuj ponownie.")
            currency = input("Podaj walutę faktury: ")
            while True:
                issue_date = input("Podaj datę wystawienia faktury (YYYY-MM-DD): ")
                if validate_date(issue_date):
                    break
                else:
                    print("Błędny format daty. Spróbuj ponownie.")
            payments = []
            while True:
                add_payment = input("Czy chcesz dodać płatność? (tak/nie): ")
                if add_payment.lower() == "tak":
                    while True:
                        payment_amount_text = input("Podaj kwotę płatności: ")
                        if validate_amount(payment_amount_text):
                            payment_amount = float(payment_amount_text)
                            break
                        else:
                            print("Błędna kwota. Spróbuj ponownie.")
                    payment_currency = input("Podaj walutę płatności: ")
                    while True:
                        payment_date = input("Podaj datę płatności (YYYY-MM-DD): ")
                        if validate_date(payment_date):
                            break
                        else:
                            print("Błędny format daty. Spróbuj ponownie.")
                    payments.append({"amount": payment_amount, "currency": payment_currency, "payment_date": payment_date})
                elif add_payment.lower() == "nie":
                    break
            invoices_data.append({"amount": amount, "currency": currency, "issue_date": issue_date, "payments": payments})
            add_invoice = input("Czy chcesz dodać kolejną fakturę? (tak/nie): ")
            if add_invoice.lower() == "nie":
                break
    else:
        print("Nieznany tryb. Spróbuj ponownie.")
        return

    for invoice_data in invoices_data:
        invoice = Invoice(invoice_data["amount"], invoice_data["currency"], invoice_data["issue_date"])

        for payment_data in invoice_data["payments"]:
            invoice.add_payment(Payment(payment_data["amount"], payment_data["currency"], payment_data["payment_date"]))

        total_payment = invoice.calculate_total_payment()

        data = ''
        for payment in invoice.payments:
            difference = calculate_difference(invoice, payment)
            print(f'Różnica w kursach walut dla płatności z dnia {payment.payment_date} wynosi: {difference}')
            data += f'Różnica w kursach walut dla płatności z dnia {payment.payment_date} wynosi: {difference}\n'

        data += f'Całkowita płatność w PLN wynosi: {total_payment}\n'

        save_to_file('output.txt', data)

        print(f'Całkowita płatność w PLN wynosi: {total_payment}')

if __name__ == "__main__":
    main()
