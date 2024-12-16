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

            
        
with open('input_file.txt', 'r') as file:
    sigma = []
    for line in file:
        line = line.strip()
        if "." not in line:
            break
        sigma.append(list(line))

x = 0
y= 0 
for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        if sigma[i][j] == "^":
            x = i
            y = j
positions = set()
obs = 0
duplicate_found = False

while True:
    for i in range(len(sigma)):
        if duplicate_found:
            break
        for j in range(len(sigma[0])):
            directions = []
            if sigma[x][y] == sigma[i][j]:
                continue
            else:
                sigma[i][j] = "#"
            
            char = sigma[x][y]
            new_x, new_y = direction(char, x, y)
            if (new_x < 0 or new_x > len(sigma)-1 or new_y < 0 or new_y > len(sigma[0])-1):     
                break
            
            if sigma[new_x][new_y] == "#":
                char = switchto(char)
            else:
                x, y = new_x, new_y
                directions.append(x+y)
                sigma[x][y] = char
            
            positions.add((x, y))
            
            if len(directions) != len(set(directions)):
                obs += 1
                duplicate_found = True
                break
    
    if duplicate_found:
        break


