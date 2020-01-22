# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com

import numpy as np

def load():
    """Funkcja do ładownaia danych ze standardowego wejścia o 'działce'"""

    wymiary = input("Wprowadź wymiary tablicy w formacie 'wiersze'x'kolumny': ")
    wymiary = wymiary.split('x')
    szer, wys = int(wymiary[1]), int(wymiary[0])
    matrix = np.zeros((wys,szer), int)
    print("Wprowadź dane wiersz po wierszu, gdzie _ wolne pole X to bagno:")
    for i in range(wys):
        str = input('')
        if(str.__len__()!=szer):
            print("Błąd wprowadzania danych")
            break
        for j in range(szer):
            if str[j] == 'x' or str[j]=='X' or str[j]=='1':
                matrix[i][j] = 1
    return matrix



