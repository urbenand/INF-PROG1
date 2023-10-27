# Function to visualize the grid
def visualize_grid(grid):
    for row in grid:
        row_str = ''.join(['.' if val == 0 else str(val) for val in row])
        print(row_str)


# This generates a 10x10 Grid/Raster, filled with 0.
grid = [[0 for _ in range(10)] for _ in range(10)]


# create blood vessel dictionary, defined like the following:
# vessel: [x1,y1,x2,y2]

blood_vessels = [
    [0, 9, 5, 9],
    [8, 0, 0, 8],
    [9, 4, 3, 4],
    [2, 2, 2, 1],
    [7, 0, 7, 4],
    [6, 4, 2, 0],
    [0, 9, 2, 9],
    [3, 4, 1, 4],
    [0, 0, 8, 8],
    [5, 5, 8, 2]
]

# create list for sub points
sub_points = []

for [x1,y1,x2,y2] in blood_vessels:

    # vertical / horizontal blood vessels
    if x1 == x2 or y1 == y2:

        # define start and endpoint of a blood vessel
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        # iterate through x axis
        for x in range(min_x, max_x + 1):

            # iterate through y axis
            for y in range(min_y, max_y + 1):

                # update grid[y][x]
                grid[x][y] += 1

visualize_grid(grid)

# count overlaps
overlap_count = 0

for row in grid:
    for column in row:
        if column >= 2:
            overlap_count += 1

print(f"There are {overlap_count} overlapping blood vessels")


