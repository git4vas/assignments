from sudoku import Sudoku
puzzle = Sudoku(3,4).difficulty(0.9)
puzzle.show()
solved = puzzle.solve()
solved.show()