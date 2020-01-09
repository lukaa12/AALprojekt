import brutal
import generator
import loadTab
import numpy as np

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
    maxFence = brutal.Fence()
    for y in range(h):
        for x in range(w):
            if arr[y,x] == 0:
                left[y,x], up[y,x] = 1, 1
                if y > 0:
                    up[y,x] += up[y-1,x]
                if x > 0:
                    left[y, x] += left[y, x-1]

    for y in range(h - 1, 0, -1):
        for x in range(w - 1, 0, -1):
            ph, pw = up[y,x], left[y,x]#potential height & width
            if ph <= 1 or pw <= 1:
                continue
            if (ph-1+pw-1)*2 <= maxFence.getLen():
                continue
            lptr = x -left[y,x] + 1
            uptr = y - up[y,x] + 1
            while lptr < x:
                rptr = uptr
                while rptr < y:
                    height = x -rptr+1
                    width = y -lptr+1
                    if up[y,lptr] >= height and left[rptr,x] >= width:
                        if (width-1+height-1) * 2 > maxFence.getLen():
                            maxFence.y1, maxFence.x1, maxFence.y2, maxFence.x2 = rptr, lptr, y, x
                        break
                    rptr = rptr + 1
                lptr = lptr +1
    return maxFence

# arr = generator.generate(5,5,0.0)
# print(fenceSize(0,0,2,2))
arr = loadTab.load()
# print(arr)
# print('-------------------')
fencePredicted = func(arr)
fencePredicted.show()