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

def main():
    while True:
        try:
            invoice_amount = float(input("Podaj kwotę faktury: "))
            invoice_currency = input("Podaj walutę faktury: ")
            invoice_issue_date = input("Podaj datę wystawienia faktury (YYYY-MM-DD): ")

            invoice = Invoice(invoice_amount, invoice_currency, invoice_issue_date)

            while True:
                add_payment = input("Czy chcesz dodać płatność? (tak/nie): ")
                if add_payment.lower() == "tak":
                    while True:
                        try:
                            payment_amount = float(input("Podaj kwotę płatności: "))
                            payment_currency = input("Podaj walutę płatności: ")
                            payment_date = input("Podaj datę płatności (YYYY-MM-DD): ")

                            invoice.add_payment(Payment(payment_amount, payment_currency, payment_date))
                            break
                        except Exception as e:
                            print(f'Wystąpił błąd: {e}. Spróbuj ponownie.')
                elif add_payment.lower() == "nie":
                    break

            total_payment = invoice.calculate_total_payment()

            data = ''
            for payment in invoice.payments:
                difference = calculate_difference(invoice, payment)
                print(f'Różnica w kursach walut dla płatności z dnia {payment.payment_date} wynosi: {difference}')
                data += f'Różnica w kursach walut dla płatności z dnia {payment.payment_date} wynosi: {difference}\n'

            data += f'Całkowita płatność w PLN wynosi: {total_payment}\n'

            save_to_file('output.txt', data)

            print(f'Całkowita płatność w PLN wynosi: {total_payment}')
            break
        except Exception as e:
            print(f'Wystąpił błąd: {e}. Spróbuj ponownie.')

if __name__ == "__main__":
    main()
