# Autor: Lukasz Wolanin
# Email: 01133389@pw.edu.pl lub lukaszwolanin98@gmail.com

from sys import argv
from time import gmtime, strftime, process_time_ns
from math import floor
from statistics import mean
import matplotlib.pyplot as plt
import numpy as np
from loadTab import load
from generator import generate
from brutal import brutal
from function import func, optimal
from fence import Fence, check



def usageHelp():
    print("Usage: -m1 \nor -m2 -n{width}x{height} -d{density}\n"
          "or -m3 -n{start size} -k{tests quantity} -step{step} -r{repeats for one size}")
    exit(-1)


def test(start, step, repeat, total):
    """Funkcja do przeprowdzania testów z pomiarem czasów wykonania"""

    timeAvgs = list()
    size = list()
    testOK = True


    for i in range(start, start + total // repeat * step, step):
        timeProbes = list()
        size.append(i)

        for j in range(repeat):
            density = np.random.rand()
            matrix = generate(i,i,density)
            startT = process_time_ns()
            out = optimal(matrix)
            stopT = process_time_ns()
            timeProbes.append(stopT-startT)
            if  not check(matrix,out):
                print("Błąd, funkcja optymalna zwróciła niedopuszczalne rozwiązanie")
                print(matrix)
                print("---------------------")
                out.show()
                return False
            if out.getLen() < func(matrix).getLen():
                print("Błąd, funkcja optymalna zwróciła poprawne, ale nie najlepsze roziązanie")
                print(matrix)
                print("---------------------")
                out.show()
                return False

        timeAvgs.append(mean(timeProbes))

    plt.plot(size, timeAvgs)
    if testOK:
        print("Tests passed")
    else:
        print("Error has occured")

    nMed = size[floor(size.__len__() // 2)]
    timeMed = timeAvgs[(int)(nMed-start)//step]
    c = nMed**2 / timeMed
    print("Algorytm z asymptotą O(T(n))")
    print("n\t\tt(n)[ms]\t\tq(n)")
    for i in  range(size.__len__()):
        q = c * timeAvgs[i] / size[i]**2
        print(size[i], "\t",  timeAvgs[i]//1000000,"ms\t\t", round(q,3))

    plt.show()


if __name__== "__main__":
    argLen = argv.__len__()

    if argLen == 2 and argv[1] == '-m1':
        matrix = load()
        result = optimal(matrix)
        result.show()
        result1 = func(matrix)
        result1.show()

    elif argLen == 4 and argv[1] == '-m2':
        wymiary = argv[2][2:]
        wymiary = wymiary.split('x')
        szer, wys = int(wymiary[0]), int(wymiary[1])
        matrix = generate(wys,szer,float(argv[3][2:]))


    elif argLen == 6 and argv[1] == '-m3':
        if argv[2][:2] != '-n' or argv[3][:2] != '-k' or argv[4][:5] != '-step' or argv[5][:2] != '-r':
            usageHelp()
        start = argv[2][2:]
        repeat = argv[5][2:]
        total = argv[3][2:]
        step = argv[4][5:]
        test(int(start),int(step),int(repeat),int(total))

    else:
        usageHelp()
