def euler15(dim):
    """Finds the number of paths from the top left to the bottom right of a dim x dim grid."""
    grid = [[0] * (dim+1)] * (dim+1)
    for row in xrange(dim, -1, -1):
        for col in xrange(dim, -1, -1):
            if row == dim and col == dim:
                grid[row][col] = 0
                continue
            if row == dim or col == dim:
                grid[row][col] = 1
                continue

            right_value = grid[row][col+1]
            below_value = grid[row+1][col]
            grid[row][col] = right_value + below_value
    
    return grid[0][0]

print euler15(20)