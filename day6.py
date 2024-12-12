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
    else:
        return r, c  
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

for i in range(100000):
    char = sigma[x][y]
    new_x, new_y = direction(char, x, y)
    if (new_x > len(sigma)-1 or new_y > len(sigma[0])-1):
        break
    if sigma[new_x][new_y] == "#":
        char = switchto(char)
    else:
        x, y = new_x, new_y
    sigma[x][y] = char
    positions.add(int(str(x)+ str(y)))
print(len(positions))
