import numpy as numpy

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,2,0,0,6],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

def possible(row, colum, number):
    global grid
    #is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    #is the number appearing in the given colum?
    for i in range(0,9):
        if grid[i][colum] == number:
            return False


    #is the number appearing in the given square?
    x0 = (colum // 3) * 3
    y0 = (row //3 ) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False

    return True


def solve():
    global grid
    for row in range(0,9):
        for colum in range(0,9):
            if grid[row][colum] ==0:
                for number in range(1,10):
                    if possible(row, colum, number):
                        grid[row][colum] = number
                        solve()
                        grid[row][colum] = 0
                return


    print(np.matrix(grid))
    input('More possible solutionns')


solve()                                

