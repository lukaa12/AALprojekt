import numpy
import loadTab
import generator

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
        print(f"Max: {self.len} ({self.y1},{self.x1})-({self.y2},{self.x2})")


def brutal(arr):
    """Funkcja znajdująca najdłuższe możliwe do ustawienia ogrodzenie metodą brute force"""

    h, w = arr.shape
    max = Fence()
    # max2 = [0, 0, 0, 0, 0]
    for y1 in range(h-1):
        for x1 in range(w-1):
            for y2 in range(y1+1,h):
                for x2 in range(x1+1,w):
                    if sum(arr[y1,x1:x2+1])+sum(arr[y2,x1:x2+1])+sum(arr[y1+1:y2,x1])+sum(arr[y1+1:y2,x2])==0:
                        # if x1 == 0 and y1 == 1 and x2 == 2 and y2 == 2:
                        #     print("HALO! ", (y2-y1+x2-x1)*2, max2[0])
                        if (y2-y1+x2-x1)*2 > max.len:
                        # if (y2 - y1 + x2 - x1) * 2 > max2[0]:
                        #     max = Fence(x1,y1,x2,y2)
                            max.x1, max.y1, max.x2, max.y2 = x1, y1, x2, y2
                            max.len = (y2-y1+x2-x1)*2
                            # max2 = [(y2-y1+x2-x1)*2, y1, x1, y2, x2]
    # print(f"Max: {max2[0]} ({max2[1]},{max2[2]})-({max2[3]},{max2[4]})")
    return max

maxi = brutal(loadTab.load())
maxi.show()


