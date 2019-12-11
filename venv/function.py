import brutal
import generator
import numpy as np

def func(arr):
    """Funkcja do znajdowania ogrodzenia, lepsza od metody brutalnej"""

    h, w = arr.shape
    max = brutal.Fence()
    for y in range(h - 1):
        for x in range(w - 1):
            sum = 0
            a, b = y, x
            if arr[y,x]+arr[y+1,x]+arr[y,x+1]==0:
                while b+1<w and arr[y,b+1]==0:
                    b=b+1
                while a+1<h and arr[a+1,b]==0 and arr[a+1,x]==0:
                    a=a+1
   #             if sum(arr[a,x:b])+0==0:
                max.x1, max.y1, max.x2, max.y2 = x, y, b, a
                max.show()
                print(x,y,a,b,max.len)

                return

arr = generator.generate(5,4,0.0)
print(arr)
func(arr)