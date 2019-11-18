import sys
import loadTab
import generator
import brutal

argLen = sys.argv.__len__()

if argLen == 2 and sys.argv[1] == '-m1':
    matrix = loadTab.load()
    result = brutal.brutal(matrix)
    result.show()

elif argLen == 4 and sys.argv[1] == '-m2':
    wymiary = sys.argv[2].split('x')
    szer, wys = int(wymiary[0]), int(wymiary[1])
    matrix = generator.generate(wys,szer,float(sys.argv[3]))
    print(matrix)
    result = brutal.brutal(matrix)
    result.show()

elif argLen == 6 and sys.argv[1] == '-m3':
    null
    #TODO

else:
    print("Usage: -m1 or -m2 widthxheight density")
    exit(-1)