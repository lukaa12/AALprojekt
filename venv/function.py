import generator
import loadTab
import numpy as np
from fence import Fence
from time import gmtime, strftime
import brutal

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
    print(type(left))
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
            for lptr in range(x - left[y, x] +1, x, 1):
                for uptr in range(y - up[x, y] +1, y, 1):
                    if (x - lptr + y - uptr) * 2 <= maxFence.getLen():
                        break
                    if up[lptr, x] > y - uptr and left[y, uptr] > x - lptr: #???
                        maxFence.reset(y, x, uptr, lptr)
    return maxFence

if __name__ == "__main__":
    arr = generator.generate(5,5,0.2)
    np.save("array" + strftime("%m%d%H%M%S", gmtime()), arr)
    # print(fenceSize(0,0,2,2))
    # arr = loadTab.load()
    print(arr)
    # print('-------------------')
    fencePredicted = func(arr)
    fencePredicted.show()
    fencePredicted = brutal.brutal(arr)
    fencePredicted.show()
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)