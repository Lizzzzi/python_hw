# array transposition

arr = [[1, 2, 4, 3],
       [5, 6, 8, 9],
       [0, 0, 0, 0],
       [11, 7, 0, 7]]

# 1  list of tuple:
array = list(zip(*arr))
print(array)

# 1.1  arr rotation 90 grad counterwise
array = list(zip(*arr))[::-1]
print(array)

# 2
tranpose = [[arr[i][j] for i in range(4)] for j in range(4)]

print(tranpose)

# yield
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

print(simpleGeneratorFun())
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)
