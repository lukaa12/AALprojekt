# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com

import generator
import loadTab
import numpy as np
from fence import Fence
from time import gmtime, strftime
import brutal
import copy


def optimal(arr):
    """Algorytm optymalny

    Działanie algorytmu jest następujące. Dla każdego wiersza zaczynając od dołu przechodzi przez niego i odpowiednio
    dla każdego elementu wpisuje numer grupy do której należy. Grupy są ciągami pól wolnych, które zcynają się w
    pierwszej kolumnie wiersza lub po wystąpieniu bagna, a kończą na ostatniej kolumnie lub przed wystąpieniem bagna.
    Dla przykładu następujący wiersz [--X---XX--X] zostanie pogrupowany: [11_222__33_]
    Następnie dla wszystkich wierszy położonych wyżej od obecnie rozpatrywanego zostaną w kolumnach zorpropagowane
    wartości grup według wzoru, że jeśli punkt wiersz niżej rozpatrywanego punktu (który nie jest zajęty) należy
    do danej grupy to punkt rozpatrywany też do niej należy Na koniec musimy tylko jeszcze raz przejść po wierszach i
     sprawdzić czy są tam możliwości stworzenia ogrodzenia np. [11___1X_1_X22] mamy dwa możliwe ogrodzenia: jedno o
     szerokości 6 z grupy 1 i drugie o szerokości 2 z grupy 2. Tak otrzymamy wszystkie możliwe ogrodzenia, musimy tylko
     zapamiętać i zwrócić to najlepsze."""

    maxFence = Fence()
    maxLenght = 0
    print(arr)
    for i in range(arr.shape[0]-1, 0, -1):
        group = 2
        for j in range(arr.shape[1]):
            if arr[i, j] == 1 and j != 0 and arr[i, j-1] != 1:
                group = group + 1
            if arr[i, j] != 1:
                arr[i, j] = group
        for row in range(i-1, -1, -1):
            for col in range(arr.shape[1]):
                if arr[row, col] == 0 and arr[row+1, col] >= 2:
                    arr[row, col] = arr[row+1, col]
        print(arr)
        for row in range(i):
            activGroup = -1
            left, right = -1, -1
            for col in range(arr.shape[1]):
                if left == -1:
                    if arr[row, col] >= 2:
                        left = col
                        activGroup = arr[row, col]
                    continue
                else:
                    if arr[row, col] == activGroup:
                        right = col
                        if right > left and maxFence.getLen() <= (right-left+i-row)*2:
                            maxLenght = (right-left+i-row)*2
                            maxFence.reset(row, left, i, right)
                    if arr[row, col] >= 2 and arr[row, col] != activGroup:
                        left = col
                        activGroup = arr[row, col]
                    if arr[row, col] == 1:
                        left = -1

    return maxFence



def func(arr):
    """Funkcja do znajdowania ogrodzenia, lepsza od metody brutalnej

    Działa najpierw tworząc dwie pomocnicze tablice o wielkości m x n w których przechowuje dla każdej
    pozycji na polu które 'grodzimy' informację ile pozyji do góry i analogicznie w prawo jest pustych
    (nie zajmowanych przez bagno), jeśli na danej pozycji jest bagno to wartości w obu tablicach dla
    niej będą równe 0.
    Następnie zaczynając od lewego dolnego rogu przechodzi macierz i dla każdej pozycji (na podstawie
    pomocniczych tablic) sprawdza ile potencjalnie można do góry i w prawo wyznaczyć dwie ścianki płotu.
    Następnie sprawdza pozycje górną prawą i dolną lewą, czy można w nich wyznaczyć kolejne dwie ścianki płotu.
    Jeśli się okaże, że już wcześniej algorytm znalazł inne większe ogrodzenie niż może znaleźć dalej badając
    aktualną pozycję, to przechodzi on do sprawdzania kolejnej."""

    left = np.zeros(arr.shape, int)
    up = np.zeros(arr.shape, int)
    h, w = arr.shape
    maxFence = Fence()
    for y in range(h):
        for x in range(w):
            if arr[y,x] == 0:
                left[y,x], up[y,x] = 1, 1
                if y > 0:
                    up[y,x] += up[y-1,x]
                if x > 0:
                    left[y, x] += left[y, x-1]
            else:
                left[y, x], up[y, x] = 0, 0

    for y in range(h-1,0,-1):
        for x in range(w-1,0,-1):
            if left[y, x] <= 1 or up[y, x] <= 1:
                continue
            if (left[y, x] + up[y, x] -2) * 2 <= maxFence.getLen():
                continue
            for uptr in range(y - up[y, x] + 1, y, 1):
                for lptr in range(x - min(left[y, x],left[uptr,x]) +1, x, 1):

                    if (x - lptr + y - uptr) * 2 <= maxFence.getLen():
                        break
                    width, height = x - lptr + 1, y - uptr +1
                    if up[y, lptr] >= height and left[uptr, x] >= width:
                        maxFence.reset(uptr, lptr, y, x)

    return maxFence



if __name__ == "__main__":
    pole = loadTab.load()
    out = optimal(pole)
    out.show()
