import math

try:
    x1, y1 = map(float, input("Podaj współrzędne pierwszego punktu (x y): ").split())
    x2, y2 = map(float, input("Podaj współrzędne drugiego punktu (x y): ").split())
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Odległość między punktami wynosi: {distance}")
except ValueError:
    print("Nieprawidłowe dane wejściowe.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
