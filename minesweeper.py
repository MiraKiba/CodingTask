def count_adjacent_mines(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and grid[i][j] == '#':
                count += 1
                
    return count

def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '-':
                grid[i][j] = str(count_adjacent_mines(grid, i, j))

    return grid

# Example grid
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Testing the function
result = minesweeper(grid)
for row in result:
    print(row)