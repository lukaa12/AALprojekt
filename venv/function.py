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

def func2(arr):
    left = np.zeros(arr.shape, int)
    up = np.zeros(arr.shape, int)
    right = np.zeros(arr.shape, int)
    down = np.zeros(arr.shape, int)
    h, w = arr.shape
    maxFence = Fence()
    for y in range(h):
        for x in range(w):
            if arr[y, x] == 0:
                left[y, x], up[y, x] = 1, 1
                if y > 0:
                    up[y, x] += up[y - 1, x]
                if x > 0:
                    left[y, x] += left[y, x - 1]
            else:
                left[y, x], up[y, x] = 0, 0

    for y in range(h-1, -1, -1):
        for x in range(w-1, -1, -1):
            if arr[y, x] == 0:
                right[y, x], down[y, x] = 1, 1
                if y < h - 1:
                    down[y, x] += down[y + 1, x]
                if x < w -1:
                    right[y, x] += right[y, x + 1]
            else:
                right[y, x], down[y, x] = 0, 0
    # print(arr)
    # print(right)
    # print(down)
    for y in range(h-1,0,-1):
        for x in range(w-1,0,-1):
            if left[y, x] <= 1 or up[y, x] <= 1:
                continue
            if (left[y, x] + up[y, x] -2) * 2 <= maxFence.getLen():
                continue
            uptr = y - up[y, x] + 1
            lptr = x - left[y, x] + 1
            while true:
                horizontal, vertical = right[uptr, lptr] >= left[y, x], down[uptr, lptr] >= up[y, x]
                if horizontal and vertical:
                    maxFence.reset(uptr, lptr, y, x)
                    break
                if horizontal and not vertical:
                    --lptr
                if not horizontal and vertical:
                    --uptr
                if not horizontal and not vertical:
                    null



def check(arr, fence):
    if fence.getLen() == 0:
        return True
    if sum(arr[fence.y1, fence.x1:fence.x2 + 1]) + sum(arr[fence.y2, fence.x1:fence.x2 + 1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x2]) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    arr = generator.generate(10,20,0.3)
    np.save("matrices/array" + strftime("%m%d%H%M%S", gmtime()), arr)
    print(arr)
    fencePredicted = func(arr)
    fencePredicted.show()
    fencePredicted = brutal.brutal(arr)
    fencePredicted.show()