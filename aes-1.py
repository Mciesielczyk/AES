from re import A
from unidecode import unidecode

S_BOX = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ]

RCON = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00],
    [0x6C,0x00, 0x00, 0x00],
    [0xD8,0x00, 0x00, 0x00]
]
def transponuj_macierz(macierz):
    transponowana = [[macierz[j][i] for j in range(len(macierz))] for i in range(len(macierz[0]))]
    return transponowana

def tekstMatrix(tekst):
    matrix = [[0, 0, 0, 0] for _ in range(4)] 
    index = 0
    for i in range(4):
        for j in range(4):
            if index < len(tekst):
                matrix[j][i] = ord(tekst[index]) 
                index += 1
    return matrix

def addRoundKey(macierzTekst, macierzKlucz):
  for i in range(4):
        for j in range(4):
            macierzTekst[i][j] ^= macierzKlucz[i][j]
            macierzTekst[i][j] = hex(macierzTekst[i][j])[2:].upper().zfill(2)

  return macierzTekst

def subBytes(macierz):
    for i in range(4):
        for j in range(4):
            row = macierz[i][j][0]
            col = macierz[i][j][1]
            if row.isdigit():
                row = int(row)
            else: row = ord(row) - ord('A') + 10
            
            if col.isdigit():
                col = int(col)
            else: col = ord(col) - ord('A') + 10

            macierz[i][j] = S_BOX[row][col]
    return macierz

def shiftRows(macierz):
    macierz[1]=macierz[1][1:]+macierz[1][:1]
    macierz[2]=macierz[2][2:]+macierz[2][:2]
    macierz[3]=macierz[3][3:]+macierz[3][:3]
    return macierz

def xtime(x):
    shifted = x << 1
    if x & 0x80:  
        shifted ^= 0x11B 
    return shifted & 0xFF

def mixColumns(state):
    result = [[0] * 4 for _ in range(4)]
    for j in range(4):
        a = [state[i][j] for i in range(4)]
        result[0][j] = xtime(a[0])^(xtime(a[1])^a[1])^a[2]^a[3]
        result[1][j] = a[0] ^ xtime(a[1])^xtime(a[2])^a[2]^a[3]
        result[2][j] = a[0] ^ a[1] ^ xtime(a[2]) ^ xtime(a[3])^a[3]
        result[3][j] = xtime(a[0])^a[0]^a[1]^a[2]^xtime(a[3])
        
    return result

def rot_word(word):
    return word[1:] + word[:1]

def sub_word(slowo):
    zamienione_slowo = []

    for bajt in slowo:
        wysokie_bity = bajt >> 4
        niskie_bity = bajt & 0x0F
        zamieniony_bajt = S_BOX[wysokie_bity][niskie_bity]
        zamienione_slowo.append(zamieniony_bajt)

    return zamienione_slowo


def xor_words(slowo1, slowo2):
    wynik_slowo = []

    for bajt1, bajt2 in zip(slowo1, slowo2):
        wynik_bajt = bajt1 ^ bajt2
        wynik_slowo.append(wynik_bajt)

    return wynik_slowo


def obliczKlucze(klucz, liczbaRund):
    w = []
    for i in range(4):
        w.append(klucz[i])

    for i in range(4, 4 * (liczbaRund + 1)):
        temp = w[i - 1]

        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp = xor_words(temp, RCON[i // 4 - 1])

        w.append(xor_words(w[i - 4], temp))
        
    return w

def stworz_macierz(w, indeks):
    poczatek = (indeks) * 4
    wybrane_slowo = w[poczatek:poczatek + 4]
    macierz = []
    for i in range(4):
        macierz.append(wybrane_slowo[i])

    return macierz

def main():
    print("Przyklad: Kodowanie tekstu 'Two One Nine Two' z kluczem 'Thats my Kung Fu' oraz 10 rundami.")
    tekst_przyklad = "Two One Nine Two"
    tekst_przyklad = "żłóóźr"
    #tekst_przyklad = ".#$  &(!)"
    #tekst_przyklad = "7"

    tekst_przyklad = unidecode(tekst_przyklad)
    klucz_przyklad = "Thats my Kung Fu"
    rundy_przyklad = 10

    print("\nKodowanie przykladu:")

    tekst_nowy = None
    macierzTekst = tekstMatrix(tekst_przyklad)
    macierzKlucz = tekstMatrix(klucz_przyklad)
    print(macierzTekst)
    print(macierzKlucz)
    for i in range(rundy_przyklad):
        if tekst_nowy is None:
            tekst_nowy = kodowanie_aes(tekst_przyklad, klucz_przyklad, rundy_przyklad, i)
        else:
            tekst_nowy = kodowanie_aes(tekst_nowy, klucz_przyklad, rundy_przyklad, i)

def kodowanie_aes(tekst, klucz, liczba_rund,i):
    if i==0:
        macierzTekst = tekstMatrix(tekst)
    else:
        macierzTekst = tekst
    macierzKlucz = tekstMatrix(klucz)
    macierzKluczOd = transponuj_macierz(macierzKlucz)
    w = obliczKlucze(macierzKluczOd, liczba_rund)
  
    if(i!=0):
        macierzKlucz=stworz_macierz(w,i)
        macierzKlucz=transponuj_macierz(macierzKlucz)

    macierz = addRoundKey(macierzTekst, macierzKlucz)
    print("\nPo operacji AddRoundKey:")
    for wiersz in macierz:
        print(" ".join(wiersz))

    macierz = subBytes(macierz)
    print("\nPo operacji SubBytes:")
    for row in macierz:
        print([hex(x) for x in row])

    macierz = shiftRows(macierz)
    print("\nPo operacji ShiftRows:")
    for row in macierz:
        print([hex(x) for x in row])
    if(i!=liczba_rund-1):
        macierz = mixColumns(macierz)
        print("\nPo operacji MixColumns:")
        for row in macierz:
            print([hex(x) for x in row])
    else: 
        macierzKlucz=stworz_macierz(w,i+1)
        macierzKlucz=transponuj_macierz(macierzKlucz)
        macierz = addRoundKey(macierzTekst, macierzKlucz)
        print("\nZakodowany tekst po wszystkich rundach: ")
        for wiersz in macierz:
            print(" ".join(wiersz))
    result = ""
    for k in range(4):  
        for j in range(4): 
            result +=str(macierz[j][k])
    print()
    print(result)
    print("--------------------------------",i+1)
    return macierz

main()
