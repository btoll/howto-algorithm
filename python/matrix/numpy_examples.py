import numpy


matrix = numpy.matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

transposed = numpy.transpose([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

print("matrix", matrix)
print("matrix.shape", matrix.shape)
print("transposed (or matrix.T)", transposed)
