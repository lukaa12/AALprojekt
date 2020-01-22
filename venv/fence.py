# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com


class Fence:
    """Klasa zawierająca informacje o prostokątnym ogrodzeniu

    x1,y1 - współrzędne pierwszego wierzchołka
    x2,y2 - współrzędne drugiego wierzchołka
    len - długość ogrodzenia"""

    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1
    len = 0

    def __init__(self, x1=-1, y1=-1, x2=-1, y2=-1):
        self.x1, self.x2, self.y1, self.y2 = x1, x2, y1, y2
        len = (y2-y1+x2-x1)*2

    def show(self):
        self.len = (self.y2 - self.y1 + self.x2 - self.x1) * 2
        if self.len > 0:
            print(f"Max: {self.len} ({self.y1},{self.x1})-({self.y2},{self.x2})")
        else:
            print("Nie znaleziono miejsca na ogrodzenie na działce")

    def getLen(self):
        if -1<self.x1 and self.x1<self.x2 and -1<self.y1 and self.y1<self.y2:
            self.len = (self.y2 - self.y1 + self.x2 - self.x1) * 2
        return self.len

    def reset(self, y1, x1, y2, x2):
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.len = (self.y2 - self.y1 + self.x2 - self.x1) * 2


def check(arr, fence):
    """Funkcja do sprawdzania czy rozwiązanie jest dopuszczalne"""

    if fence.getLen() == 0:
        return True
    if sum(arr[fence.y1, fence.x1:fence.x2 + 1]) + sum(arr[fence.y2, fence.x1:fence.x2 + 1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x1]) + sum(arr[fence.y1 + 1:fence.y2, fence.x2]) == 0:
        return True
    else:
        return False

