# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com

from fence import Fence

def brutal(arr):
    """Funkcja znajdująca najdłuższe możliwe do ustawienia ogrodzenie metodą brute force.

    Działa rozpatrując wszystkie możliwe kombinacje punktów, dla każdej sprawdzając sumę
    elementów leżących na krawędziach wyznaczonych przez punkty leżące na przekątnej.
    Złożoność czasowa = O(n^3*m^3) gdzie n i m to liczba wierszy i kolumn
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



