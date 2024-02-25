def is_prime():
    try:
        num = int(input("Podaj liczbę: "))
        if num < 2:
            print("Liczba musi być większa niż 2.")
            return
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"Liczba {num} nie jest liczbą pierwszą.")
                return
        print(f"Liczba {num} jest liczbą pierwszą.")
    except ValueError:
        print("Nieprawidłowe dane wejściowe.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

is_prime()
