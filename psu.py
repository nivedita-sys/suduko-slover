
import numpy as np 
suduko = []
print("Please use 0 in place of blank spaces")
for i in range(9):
    row = list(input("Enter the elements of row {} without any spaces and commas: ".format(i+1)))
    row = [int(i) for i in row]
    suduko.append(row)

# Display a message before showing the Sudoku grid
print("\nThis is the Sudoku puzzle you entered:\n")
print(np.matrix(suduko))

def possible(y, x, n):
    global suduko
    for i in range(0, 9):
        if suduko[y][i] == n:
            return False
    for i in range(0, 9):
        if suduko[i][x] == n:
            return False
    box_y = (y // 3) * 3
    box_x = (x // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if suduko[box_y + i][box_x + j] == n:
                return False
    return True

def solve():
    for y in range(0, 9):
        for x in range(0, 9):
            if suduko[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        suduko[y][x] = n
                        solve()
                        suduko[y][x] = 0
                return
    print("\n Now lets see the output\n")
    print("This is the solved Sudoku puzzle:")
    print("...........................................")
    print(np.matrix(suduko))
    print("...........................................")
    print("It's complete,yhhaaa!!!")

solve()
