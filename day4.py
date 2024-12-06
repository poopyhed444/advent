def get_user_input():
    data = []
    try:
        while True:
            line = input()
            data.append(line)
    except EOFError:
        pass
    return data

user_data = get_user_input()

grid = []
for line in user_data:
    row = []
    for letter in line:
        row.append(letter)
    grid.append(row)

count = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
       if grid[r][c] == "X":
        try:
            if grid[r][c+1] == "M" and grid[r][c+2] == "A" and grid[r][c+3] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r][c-1] == "M" and grid[r][c-2] == "A" and grid[r][c-3] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r-1][c] == "M" and grid[r-2][c] == "A" and grid[r-3][c] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r-1][c-1] == "M" and grid[r-2][c-2] == "A" and grid[r-3][c-3] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A" and grid[r+3][c+3] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A" and grid[r-3][c+3] == "S":
                count += 1
        except IndexError:
            pass

        try:
            if grid[r+1][c-1] == "M" and grid[r+2][c-2] == "A" and grid[r+3][c-3] == "S":
                count += 1
        except IndexError:
            pass
print(count)
