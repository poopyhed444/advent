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
        sigma.append(line)
       
	    
    except EOFError:
        break

x = 0
y= 0 
for i in range(len(sigma)):
    for j in range(len(sigma[0])):
        if sigma[i][j] == "^":
            x = i
            y = j


for i in range(100):
    char = sigma[x][y]
    print(char, x, y)
    x,y = direction(char,x,y)
    if (sigma[x][y] == "#"):
       char = switchto(sigma[x][y])
       print(sigma)
