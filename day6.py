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

while True:
    positions.add((x, y))
    char = sigma[x][y]
    new_x, new_y = direction(char, x, y)
    if (new_x < 0 or new_x > len(sigma)-1 or new_y < 0 or new_y > len(sigma[0])-1):     
           print(len(positions))
           break
    if sigma[new_x][new_y] == "#":
        char = switchto(char)
    else:
         x, y = new_x, new_y
    sigma[x][y] = char


print(len(positions))
