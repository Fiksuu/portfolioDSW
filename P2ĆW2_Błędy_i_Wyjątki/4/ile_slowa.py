def count_word_occurrences():
    try:
        word = input('Podaj słowo do wyszukania: ')
        with open('P2ĆW2_Błędy_i_Wyjątki/4/tekst.txt', 'r') as f:
            contents = f.read()
        occurrences = contents.count(word)
        print(f'Słowo {word} występuje {occurrences} razy w pliku.')
    except FileNotFoundError:
        print('Plik nie istnieje.')
    except Exception as e:
        print(f'Wystąpił błąd: {e}')

count_word_occurrences()
