def count_cars_in_grid(boxes, img_width, img_height, n_rows, n_cols):
    grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    cell_width = img_width / n_cols
    cell_height = img_height / n_rows

    for box in boxes:
        x_min, y_min, x_max, y_max = box
        center_x = (x_min + x_max) / 2
        center_y = (y_min + y_max) / 2

        col_idx = int(center_x // cell_width)
        row_idx = int(center_y // cell_height)

        col_idx = min(col_idx, n_cols - 1)
        row_idx = min(row_idx, n_rows - 1)

        grid[row_idx][col_idx] += 1

    return grid

boxes = [
    (10, 20, 50, 60), (20, 25, 55, 65), (35, 45, 75, 85), (40, 50, 80, 90), 
    (50, 60, 100, 110), (110, 120, 150, 160), (130, 140, 170, 180), 
    (160, 170, 200, 210), (175, 185, 195, 205)
]
img_width = 200
img_height = 200
n_rows = 5
n_cols = 5

grid_count = count_cars_in_grid(boxes, img_width, img_height, n_rows, n_cols)

for row in grid_count:
    print(row)

