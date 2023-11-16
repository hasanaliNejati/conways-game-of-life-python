import numpy

#nm = numpy.array([0,11,2,42])
nm = numpy.eye(6)
print(nm)

def printArray(arr):
    output = ""
    for i in arr:
        for j in i:
            output += " 1 " if j != 0 else "   "
        output += "\n"
    print (output)
    
printArray(nm) 