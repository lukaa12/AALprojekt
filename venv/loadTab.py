import numpy as np

def load():
    """Funkcja do ładownaia danych ze standardowego wejścia o 'działce'"""

    wymiary = input("Wprowadź wymiary tablicy w formacie 'szer'x'wys': ")
    wymiary = wymiary.split('x')
    szer, wys = int(wymiary[0]), int(wymiary[1])
    matrix = np.zeros((wys,szer), int)
    print("Wprowadź dane wiersz po wierszu, gdzie _ wolne pole X to bagno:")
    for i in range(wys):
        str = input('')
        if(str.__len__()!=szer):
            print("Błąd wprowadzania danych")
            break
        for j in range(szer):
            if str[j] == 'x' or str[j]=='X':
                matrix[i][j] = 1
    return matrix



