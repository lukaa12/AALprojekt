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
            #print("(%d, %d)" % (y, x))
            if left[y, x] <= 1 or up[y, x] <= 1:
                #print("\t -<1")
                continue
            if (left[y, x] + up[y, x] -2) * 2 <= maxFence.getLen():
                #print("\t -<maxFence")
                continue
            for uptr in range(y - up[y, x] + 1, y, 1):
                for lptr in range(x - left[y, x] +1, x, 1):
                    #print("\t(%d, %d)" % (uptr, lptr))
                    if (x - lptr + y - uptr) * 2 <= maxFence.getLen():
                        #print("\t -<INSIDEmaxFence")
                        break
                    width, height = x - lptr + 1, y - uptr +1
                    #print("\t\tszer: %d<=%d wys: %d<=%d" % (width, left[uptr, x], height, up[y, lptr]))
                    if up[y, lptr] >= height and left[uptr, x] >= width:
                        maxFence.reset(uptr, lptr, y, x)
                        #print("OK")

    return maxFence

def check(arr, fence):
    if fence.getLen() == 0:
        return True
    if sum(arr[fence.y1, fence.x1:fence.x2 + 1]) + sum(arr[fence.y2, fence.x1:fence.x2 + 1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x2]) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    arr = generator.generate(1000,1000,0.6)
    np.save("matrices/array" + strftime("%m%d%H%M%S", gmtime()), arr)
    # print(fenceSize(0,0,2,2))
    # arr = loadTab.load()
    print(arr)
    # print('-------------------')
    fencePredicted = func(arr)
    fencePredicted.show()
    #fencePredicted = brutal.brutal(arr)
    #fencePredicted.show()
    #fence = Fence()
    #fence.show()
    #fence.reset(0,0,4,3)
    #fence.show()