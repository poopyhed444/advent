sigma = []
def direction(pointer, r, c):
    if pointer == "^":
        return r-1, c
    if pointer == "v":
        return r+1, c
    if pointer == ">":
        return r, c+1
    if pointer == "<":
        return r, c-1
    else:
        print(pointer, r, c)

def switchto(pointer):
    if pointer == "^":
        return ">"
    if pointer == ">":
        return "v"
    if pointer == "v":
        return "<"
    if pointer == "<":
        return "^"

while True:
    try:
        line = input()
        if "." not in line:
            break
        sigma.append(list(line))
    except EOFError:
        break


for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        if sigma[i][j] == "^":
           initial_x = i 
           initial_y = j

positions = set()
original_sigma = [row[:] for row in sigma]
for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        original_char = sigma[i][j]
        sigma[i][j] = '#'
        x, y = initial_x, initial_y
        while True:
            positions.add((x, y))
            char = sigma[x][y]
            new_x, new_y = direction(char, x, y)
            print(f"char: {char}, x: {x}, y: {y}, new_x: {new_x}, new_y: {new_y}")
            if new_x < 0 or new_x >= len(sigma) or new_y < 0 or new_y >= len(sigma[0]):
                print("done")
                break
            if sigma[new_x][new_y] == "#":
                char = switchto(char)
            else:
                x, y = new_x, new_y
            sigma[x][y] = char

        
        sigma[i][j] = original_char 
        sigma = [row[:] for row in original_sigma]
