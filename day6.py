sigma = []
def direction(pointer,r,c):
    if (pointer == "^"):
        return r-1,c
    if (pointer == "v"):
        return r+1,c
    if (pointer == ">"):
        return r,c+1
    if (pointer == "<"):
        return r,c-1
def switchto(pointer):
    if (pointer == "^"):
        return ">"
    if (pointer == ">"):
        return "v"
    if (pointer == "v"):
        return "<"
    if (pointer == "<"):
        return "^"
while True:
    try:
        line = input()
        if "." not in line:
            break
        sigma.append(list(line))
       
	    
    except EOFError:
        break

x = 0
y= 0 
for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        if sigma[i][j] == "^":
            x = i
            y = j

positions = set()
original_sigma = [row[:] for row in sigma]  

for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        x, y = i, j  
        original_char = sigma[i][j]
        sigma[i][j] = '#'
        positions = set()
        print(sigma)

        while True:
            if (x, y) in positions:
                break 
            positions.add((x, y))
            char = sigma[x][y]
            if char == "#":
                print("hg")
                break
            new_x, new_y = direction(char, x, y)
            if new_x < 0 or new_x >= len(sigma) or new_y < 0 or new_y >= len(sigma[0]):     
                print("j")
                break

            if sigma[new_x][new_y] == "#":
                char = switchto(char)
            else:
                x, y = new_x, new_y
            sigma[x][y] = char

        sigma[i][j] = original_char

print("Final result:", len(positions))

