import numpy as np

def generate(h, w, p):
    fill = np.random.rand(h*w) < p
    # print(fill)
    matrix = np.zeros((h,w), int)
    for i in range(h*w):
        if fill[i]:
            matrix[i//w,i%w] = 1

    return matrix

# print(generate(4,7,0.5))