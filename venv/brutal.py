import numpy
import loadTab
import generator

def brutal(arr):
    """Funkcja znajdująca najdłuższe możliwe do ustawienia ogrodzenie metodą brute force"""

    print(arr)
    zz = 1
    h, w = arr.shape
 #   print(h,w)
    max = [0, -1, -1, -1, -1]
    for y1 in range(h-1):
        for x1 in range(w-1):
            for y2 in range(y1+1,h):
                for x2 in range(x1+1,w):
                    if sum(arr[y1,x1:x2+1])+sum(arr[y2,x1:x2+1])+sum(arr[y1+1:y2,x1])+sum(arr[y1+1:y2,x2])==0:
                        if (y2-y1+x2-x1)*2 > max[0]:
                            max = [(y2-y1+x2-x1)*2, y1, x1, y2, x2]
    print(f"Max: {max[0]} ({max[1]},{max[2]})-({max[3]},{max[4]})")

#mat = loadTab.load()

mat = generator.generate(7,10,0.2)
brutal(mat)

