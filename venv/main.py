import sys
import loadTab
import generator
import brutal

argLen = sys.argv.__len__()

if argLen not in [2, 4, 6]:
    print("Usage: ...") #TODO
    exit(-1)

if argLen == 2 and sys.argv[1] == '-m1':
    matrix = loadTab.load()
    result = brutal.brutal(matrix)
    result.show()

elif argLen == 4 and sys.argv[1] == '-m2':
    #TODO
    null