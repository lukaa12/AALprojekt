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

    maxFence = Fence()
    maxLenght = 0
    for i in range(arr.shape[0]-1, 0, -1):
        tmp = copy.deepcopy(arr)
        group = 2
        for j in range(tmp.shape[1]):
            if arr[i, j] == 1 and j != 0 and arr[i, j-1] != 1:
                group = group + 1
            if tmp[i, j] == 0:
                tmp[i, j] = group
        for row in range(i-1, -1, -1):
            for col in range(tmp.shape[1]):
                if tmp[row, col] == 0 and tmp[row+1, col] >= 2:
                    tmp[row, col] = tmp[row+1, col]

        for row in range(i):
            activGroup = -1
            left, right = -1, -1
            for col in range(tmp.shape[1]):
                if left == -1:
                    if tmp[row, col] >= 2:
                        left = col
                        activGroup = tmp[row, col]
                    continue
                else:
                    if tmp[row, col] == activGroup:
                        right = col
                        if right > left and maxFence.getLen() <= (right-left+i-row)*2:
                            maxLenght = (right-left+i-row)*2
                            maxFence.reset(row, left, i, right)
                    if tmp[row, col] >= 2 and tmp[row, col] != activGroup:
                        left = col
                        activGroup = tmp[row, col]
                    if tmp[row, col] == 1:
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

    for y in range(h-1,0,-1):
        for x in range(w-1,0,-1):
            if left[y, x] <= 1 or up[y, x] <= 1:
                continue
            if (left[y, x] + up[y, x] -2) * 2 <= maxFence.getLen():
                continue
            if left[y, x] >= up[y, x]:
                squareSide = up[y, x] - 1
                while squareSide > 0:
                    if left[y-squareSide, x] >= squareSide + 1:
                        break
                    --squareSide
                for longerSide in range(max(left[y, x],left[y-squareSide, x]) - 1, 0, -1):
                    if up[y,x-longerSide] >= squareSide + 1 and 2*(squareSide+longerSide) > maxFence.getLen():
                        maxFence.reset(y-squareSide,x-longerSide,y,x)
            if left[y, x] < up[y, x]:
                squareSide = left[y, x] - 1
                while squareSide > 0:
                    if up[y, x-squareSide] >= squareSide + 1:
                        break
                    --squareSide
                for longerSide in range(max(up[y, x],up[y, x-squareSide]) - 1, 0, -1):
                    if left[y-longerSide,x] >= squareSide + 1 and 2*(squareSide+longerSide) > maxFence.getLen():
                        maxFence.reset(y-squareSide,x-longerSide,y,x)

    for y in range(h):
        for x in range(w):
            if right[y, x] <= 1 or down[y, x] <= 1:
                continue
            if (right[y, x] + down[y, x] - 2) * 2 <= maxFence.getLen():
                continue

            if right[y, x] >= down[y, x]:
                squareSide = down[y, x] - 1
                while squareSide > 0:
                    if right[y + squareSide, x] >= squareSide + 1:
                        break
                    --squareSide
                for longerSide in range(max(right[y, x], right[y + squareSide, x]) - 1, 0, -1):
                    if down[y, x + longerSide] >= squareSide + 1 and 2 * (squareSide + longerSide) > maxFence.getLen():
                        maxFence.reset(y - squareSide, x - longerSide, y, x)

            if right[y, x] <= down[y, x]:
                squareSide = right[y, x] - 1
                while squareSide > 0:
                    if down[y, x + squareSide] >= squareSide + 1:
                        break
                    --squareSide
                for longerSide in range(max(down[y, x], down[y, x + squareSide]) - 1, 0, -1):
                    if right[y + longerSide, x] >= squareSide + 1 and 2 * (squareSide + longerSide) > maxFence.getLen():
                        maxFence.reset(y - squareSide, x - longerSide, y, x)

    return maxFence

if __name__ == "__main__":
    pole = loadTab.load()
    out = optimal(pole)
    out.show()
    out = func(pole)
    out.show()
