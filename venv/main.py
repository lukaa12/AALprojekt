import numpy as np
from time import gmtime, strftime
import sys
import loadTab
import generator
import brutal
import function

def test():
    testOK = True
    for i in [10, 20]:#, 40, 50, 70, 100, 150, 200, 300, 400, 500, 700, 900, 1000]:
        for j in [i/2, 4 * i / 5, i]:
            j = int(j)
            passed = True
            gestosc = np.random.rand(2)
            matrix = [generator.generate(i,j,gestosc[0]), generator.generate(j,i,gestosc[1])]
            out = function.func(matrix[0])
            out.show()
            if i * j <1600:
                out2 = brutal.brutal(matrix[0])
                out2.show()
                if out.getLen() != out2.getLen():
                    passed = testOK = False

            if  not function.check(matrix[0],out):
                passed = testOK = False
            okay = "testsOutput/test-Passed:"
            if not passed:
                okay = "testsOutput/test-Failed"
                print("Fail")
            np.save(okay + strftime("%m%d%H%M%S", gmtime()), matrix[0])
            # passed = True
            # out = function.func(matrix[1])
            # if i * j < 1600:
            #     out2 = brutal.brutal(matrix[1])
            #     if out.getLen() != out2.getLen():
            #         passed = False
            #
            # if not function.check(matrix[1], out):
            #     passed = False
            # okay = "-Passed:"
            # if not passed:
            #     okay = "-Failed:(" + str(out.y1) + "," + str(out.x1) + ")(" + str(out.y2) + "," + str(out.x2) + ")" + str(out.getLen())
            #     print("Fail")
            # np.save("testsOutput/test" + okay + strftime("%m%d%H%M%S", gmtime()), matrix[1])
    if testOK:
        print("Tests passed")

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

elif sys.argv[1] == '-m3': # argLen == 6 and
    test()

else:
    print("Usage: -m1 or -m2 widthxheight density")
    exit(-1)