# Szyfrowanie i deszyfrowanie AES w Pythonie

## Opis projektu
Projekt implementuje algorytm szyfrowania AES (Advanced Encryption Standard) w języku Python. Program pozwala na kodowanie i odkodowanie tekstu przy użyciu podanego klucza, wykorzystując podstawowe operacje stosowane w AES: SubBytes, ShiftRows, MixColumns i AddRoundKey.


## Struktura kodu
Program składa się z następujących funkcji:
- `transponuj_macierz(macierz)`: Transponuje podaną macierz.
- `tekstMatrix(tekst)`: Konwertuje podany tekst na macierz bajtów.
- `addRoundKey(macierzTekst, macierzKlucz)`: Dodaje klucz rundy do macierzy tekstu.
- `subBytes(macierz)`: Stosuje podstawienie bajtów zgodnie z tabelą S-Box.
- `shiftRows(macierz)`: Przesuwa wiersze macierzy zgodnie z zasadami AES.
- `xtime(x)`: Przesuwa bity w lewo i wykonuje operację XOR z wartością 0x11B, jeśli najwyższy bit jest ustawiony.
- `mixColumns(state)`: Miesza kolumny w macierzy zgodnie z operacją mnożenia w GF(2^8).
- `rot_word(word)`: Rotuje bajty w słowie.
- `sub_word(slowo)`: Podstawia bajty w słowie zgodnie z tabelą S-Box.
- `xor_words(slowo1, slowo2)`: Wykonuje operację XOR na dwóch słowach.
- `obliczKlucze(klucz, liczbaRund)`: Generuje podklucze dla każdej rundy szyfrowania.
- `stworz_macierz(w, indeks)`: Tworzy macierz klucza dla danej rundy.
- `kodowanie_aes(tekst, klucz, liczba_rund, i)`: Implementuje pełne kodowanie AES dla danej rundy.
- `main()`: Główna funkcja programu, która uruchamia przykład szyfrowania.

## Przykład użycia
```python
Przyklad: Kodowanie tekstu 'Two One Nine Two' z kluczem 'Thats my Kung Fu' oraz 10 rundami.
```
Wyniki są wyświetlane na standardowym wyjściu (konsoli) po każdej operacji w AES.

## Uruchomienie
Aby uruchomić program, wykonaj w terminalu:
```bash
python nazwa_pliku.py
```


Projekt został wykonany na przedmiot matematyka dyskretna na III semestrze.

