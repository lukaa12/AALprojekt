import numpy as np
from time import gmtime, strftime, process_time_ns
from statistics import mean
import sys
import loadTab
import generator
import brutal
import function
import matplotlib.pyplot as plt

def test(start, step, repeat, total):
    timeAvgs = list()
    size = list()
    testOK = True
    density = np.random.rand()
    for i in range(start,total//repeat*step+1,step):
        timeProbes = list()
        size.append(i)
        for density in range(repeat):
            passed = True
            matrix = generator.generate(i,i,density)
            start = process_time_ns()
            out = function.func(matrix)
            stop = process_time_ns()
            timeProbes.append(stop-start)
                #out.show()
            if i**2 <800:
                out2 = brutal.brutal(matrix)
                out2.show()
                if out.getLen() != out2.getLen():
                    passed = testOK = False
                if  not function.check(matrix,out):
                   passed = testOK = False
            if not passed:
                print("Fail")
            else:
                print("Passed")
        timeAvgs.append(mean(timeProbes))
    plt.plot(size, timeAvgs)
    plt.show()
    if testOK:
        print("Tests passed")

def usageHelp():
    print("Usage: -m1 \nor -m2 -n{width}x{height} -d{density}\n"
          "or -m3 -n{start size} -k{tests quantity} -step{step} -r{repeats for one size}")
    exit(-1)

argLen = sys.argv.__len__()

if argLen == 2 and sys.argv[1] == '-m1':
    matrix = loadTab.load()
    result = brutal.brutal(matrix)
    result.show()
    result2 = function.func(matrix)
    result2.show()

elif argLen == 4 and sys.argv[1] == '-m2':
    wymiary = sys.argv[2].split('x')
    szer, wys = int(wymiary[0]), int(wymiary[1])
    matrix = generator.generate(wys,szer,float(sys.argv[3]))
    print(matrix)
    result = brutal.brutal(matrix)
    result.show()
    result2 = function.func(matrix)
    result2.show()

elif argLen == 6 and sys.argv[1] == '-m3':
    if sys.argv[2][:2] != '-n' or sys.argv[3][:2] != '-k' or sys.argv[4][:5] != '-step' or sys.argv[5][:2] != '-r':
        usageHelp()
    start = sys.argv[2][2:]
    repeat = sys.argv[5][2:]
    total = sys.argv[3][2:]
    step = sys.argv[4][5:]
    test(int(start),int(step),int(repeat),int(total))

else:
    usageHelp()