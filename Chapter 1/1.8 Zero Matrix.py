"Given M x N matrix, set column and row of the element which has value of zero"

mat = [[1, 2, 3, 4, 5],
       [0, 2, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 0, 3, 4, 5],
       [1, 2, 3, 4, 5],
       [1, 2, 0, 4, 5],
       [1, 2, 3, 4, 0], ]

ans = [[0, 0, 0, 4, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 4, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 4, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0], ]

#Approach 1
"""
b = []
def initializeB(m, n):
    global b
    for i in range(m):
        b.append([])
        for j in range(n):
            b[i].append(-1)

def setRowToZero(x, n):
    for j in range(n):
        b[x][j] = 0

def setColToZero(m, y):
    for i in range(m):
        b[i][y] = 0


def setZero(a, m, n):
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                setRowToZero(i, n)
                setColToZero(m, j)

    for i in range(m):
        for j in range(n):
            if b[i][j] == -1:
                b[i][j] = a[i][j]



def computeZeroValues(mat, m, n):
    initializeB(m, n)
    return setZero(mat, m ,n)


computeZeroValues(mat, 7, 5)
print b
assert b == ans
"""



#Approach 2. Inplace modification

def zeroRow(n):
    x = []
    for i in range(n):
        x.append(0)
    return x

def computeZeroValues(mat, m, n):
    row1HasZero = False
    col1HasZero = False
    for i in range(m):
        if mat[i][0] == 0:
            col1HasZero = True
    for j in range(n):
        if mat[0][j] == 0:
            row1HasZero = True

    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j] == 0:
                mat[i][0] = 0
                mat[0][j] = 0

    #row
    for i in range(1, m):
        if mat[i][0] == 0:
            mat[i] = zeroRow(n)

    #column
    for j in range(1,n):
        if mat[0][j] == 0:
            for i in range(m):
                mat[i][j] = 0

    if row1HasZero:
        mat[0] = zeroRow(n)

    if col1HasZero:
        for i in range(m):
            mat[i][0] = 0

    return mat

temp = computeZeroValues(mat, 7, 5)
assert temp == ans
