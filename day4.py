# def get_user_input():
#     data = []
#     try:
#         while True:
#             line = input()
#             data.append(line)
#     except EOFError:
#         pass
#     return data

# user_data = get_user_input()

# grid = []
# for line in user_data:
#     row = []
#     for letter in line:
#         row.append(letter)
#     grid.append(row)

# count = 0
# rows = len(grid)
# cols = len(grid[0])

# for r in range(len(grid)):
#     for c in range(cols):
#         if grid[r][c] == "X":
#             if c + 3 < cols and grid[r][c+1] == "M" and grid[r][c+2] == "A" and grid[r][c+3] == "S":
#                 count += 1
#             if c - 3 >= 0 and grid[r][c-1] == "M" and grid[r][c-2] == "A" and grid[r][c-3] == "S":
#                 count += 1
#             if r + 3 < rows and grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S":
#                 count += 1
#             if r - 3 >= 0 and grid[r-1][c] == "M" and grid[r-2][c] == "A" and grid[r-3][c] == "S":
#                 count += 1
#             if r + 3 < rows and c + 3 < cols and grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A" and grid[r+3][c+3] == "S":
#                 count += 1
#             if r - 3 >= 0 and c - 3 >= 0 and grid[r-1][c-1] == "M" and grid[r-2][c-2] == "A" and grid[r-3][c-3] == "S":
#                 count += 1
#             if r - 3 >= 0 and c + 3 < cols and grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A" and grid[r-3][c+3] == "S":
#                 count += 1
#             if r + 3 < rows and c - 3 >= 0 and grid[r+1][c-1] == "M" and grid[r+2][c-2] == "A" and grid[r+3][c-3] == "S":
#                 count += 1
# print(count)

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
rows = len(grid)
cols = len(grid[0])

for r in range(len(grid)):
    for c in range(cols):
        if grid[r][c] == "A":
            if r + 1 < rows and c + 1 < cols and grid[r+1][c+1] == "S":               
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == "M":
                    if r - 1 >= 0 and c + 1 < cols and grid[r-1][c+1] == "S" :
                        if r + 1 < rows and c - 1 >= 0 and grid[r+1][c-1] == "M" :
                            count += 1
            if r + 1 < rows and c + 1 < cols and grid[r+1][c+1] == "M":               
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == "S":
                    if r - 1 >= 0 and c + 1 < cols and grid[r-1][c+1] == "M" :
                        if r + 1 < rows and c - 1 >= 0 and grid[r+1][c-1] == "S" :
                            count += 1

            if r + 1 < rows and c + 1 < cols and grid[r+1][c+1] == "M":               
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == "S":
                    if r - 1 >= 0 and c + 1 < cols and grid[r-1][c+1] == "S" :
                        if r + 1 < rows and c - 1 >= 0 and grid[r+1][c-1] == "M" :
                            count += 1   
        
            if r + 1 < rows and c + 1 < cols and grid[r+1][c+1] == "S":               
                if r - 1 >= 0 and c - 1 >= 0 and grid[r-1][c-1] == "M":
                    if r - 1 >= 0 and c + 1 < cols and grid[r-1][c+1] == "M" :
                        if r + 1 < rows and c - 1 >= 0 and grid[r+1][c-1] == "S" :
                            count += 1     
        
print(count)
