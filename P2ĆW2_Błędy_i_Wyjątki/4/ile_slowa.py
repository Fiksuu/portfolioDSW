def count_word_occurrences():
    try:
        file_path = input('Podaj ścieżkę do pliku: ')
        word = input('Podaj słowo do wyszukania: ')
        with open(file_path, 'r') as f:
            contents = f.read()
        occurrences = contents.count(word)
        print(f'Słowo {word} występuje {occurrences} razy w pliku.')
    except FileNotFoundError:
        print('Plik nie istnieje.')
    except Exception as e:
        print(f'Wystąpił błąd: {e}')

count_word_occurrences()
