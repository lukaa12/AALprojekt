import numpy


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
        if self.len > 0:
            print(f"Max: {self.len} ({self.y1},{self.x1})-({self.y2},{self.x2})")
        else:
            print("Nie znaleziono miejsca na ogrodzenie na działce")


def brutal(arr):
    """Funkcja znajdująca najdłuższe możliwe do ustawienia ogrodzenie metodą brute force.

    Zwraca obiekt klasy Fence zawierający dane znalezionego ogrodzenia."""

    h, w = arr.shape
    max = Fence()
    for y1 in range(h-1):
        for x1 in range(w-1):
            for y2 in range(y1+1,h):
                for x2 in range(x1+1,w):
                    if sum(arr[y1,x1:x2+1])+sum(arr[y2,x1:x2+1])+sum(arr[y1+1:y2,x1])+sum(arr[y1+1:y2,x2])==0:
                        if (y2-y1+x2-x1)*2 > max.len:
                            max.x1, max.y1, max.x2, max.y2 = x1, y1, x2, y2
                            max.len = (y2-y1+x2-x1)*2
    return max



