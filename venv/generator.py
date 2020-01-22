# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com

import numpy as np

def generate(h, w, p):
    """Funkcja generująca losowe dane do celów testowych.

    Przyjmująca za parametry wysokość, szerokość i stopień 'zabagnienia' pola."""

    fill = np.random.rand(h*w) < p
    matrix = np.zeros((h,w), int)
    for i in range(h*w):
        if fill[i]:
            matrix[i//w,i%w] = 1

    return matrix
