import requests
import json
import datetime

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
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)
    except Exception as e:
        print(f'Wystąpił błąd podczas zapisywania do pliku: {e}')

def load_invoices_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f'Wystąpił błąd podczas wczytywania danych z pliku: {e}')
        return []

def main():
    mode = input("Wybierz tryb (wsadowy/manualny): ")

    if mode.lower() == "wsadowy":
        filename = input("Podaj nazwę pliku z danymi: ")
        invoices_data = load_invoices_from_file(filename)
    elif mode.lower() == "manualny":
        invoices_data = [
            {
                "amount": float(input("Podaj kwotę faktury: ")),
                "currency": input("Podaj walutę faktury: "),
                "issue_date": input("Podaj datę wystawienia faktury (YYYY-MM-DD): "),
                "payments": [
                    {
                        "amount": float(input("Podaj kwotę płatności: ")),
                        "currency": input("Podaj walutę płatności: "),
                        "payment_date": input("Podaj datę płatności (YYYY-MM-DD): ")
                    }
                ]
            }
        ]
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
