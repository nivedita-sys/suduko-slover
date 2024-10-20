from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# The Sudoku solving code
def possible(suduko, y, x, n):
    for i in range(9):
        if suduko[y][i] == n or suduko[i][x] == n:
            return False
    box_y, box_x = (y // 3) * 3, (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if suduko[box_y + i][box_x + j] == n:
                return False
    return True

def solve_sudoku(suduko):
    for y in range(9):
        for x in range(9):
            if suduko[y][x] == 0:
                for n in range(1, 10):
                    if possible(suduko, y, x, n):
                        suduko[y][x] = n
                        if solve_sudoku(suduko):
                            return True
                        suduko[y][x] = 0
                return False
    return True

# The routes for the web application
@app.route("/", methods=["GET"])
def index():
    empty_sudoku = [[0 for _ in range(9)] for _ in range(9)]
    return render_template("index.html", sudoku=empty_sudoku)

@app.route("/solve", methods=["POST"])
def solve():
    # Retrieve Sudoku data from form
    suduko = []
    for i in range(9):
        row = []
        for j in range(9):
            value = request.form.get(f'cell{i}{j}')
            if value and value.isdigit():
                row.append(int(value))
            else:
                row.append(0)
        suduko.append(row)
    
    suduko = np.array(suduko)
    
    if solve_sudoku(suduko):
        solved_sudoku = suduko.tolist()
        return render_template("index.html", sudoku=solved_sudoku)
    else:
        return "Sudoku cannot be solved", 400

if __name__ == "__main__":
    app.run(debug=True)
