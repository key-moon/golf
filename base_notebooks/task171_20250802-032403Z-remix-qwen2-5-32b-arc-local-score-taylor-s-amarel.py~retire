def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    output = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                output[r][c] = 8
            else:
                output[r][c] = 0
                
    return output