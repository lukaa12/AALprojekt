import numpy

def load():
    """Funkcja do ładownaia danych o 'działce'"""

    wymiary = input("Wprowadź wymiary tablicy w formacie 'szer'x'wys': ")
    wymiary = wymiary.split('x')
    szer, wys = int(wymiary[0]), int(wymiary[1])
    matrix = numpy.zeros((wys,szer), int)
    print("Wprowadź dane wiersz po wierszu, gdzie _ wolne pole X to bagno:")
    for i in range(wys):
        str = input('')
        if(str.__len__()!=szer):
            print("Błąd wprowadzania danych")
            break
        for j in range(szer):
            if str[j] == 'x' or str[j]=='X':
                # print(i,j)
                matrix[i][j] = 1
    # print(matrix)
    return matrix

# load()

if 0:
    z = 1
    macierz = numpy.zeros((3,4), int)
    for i in range(3):
        for j in range(4):
            macierz[i][j] = (i+1)*10 + j+1

    print(macierz)
    print(macierz[0:0,0])

