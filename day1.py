
# left = []
# right = []
# try:
#     while True:
#         n, m = map(int, input().split())
#         left.append(n)
#         right.append(m)
# except EOFError:
#     pass  
# left.sort()
# right.sort()
# total = 0
# for i in range(len(left)):
#     total += abs(left[i]- right[i])

# print(total)
    

left = []
right = []
try:
    while True:
        n, m = map(int, input().split())
        left.append(n)
        right.append(m)
except EOFError:
    pass  
left.sort()
right.sort()
total = 0
for i in range(len(left)):
    count =0
    for j in range(len(left)):
        if (left[i] == right[j]): 
            count+=1
    total += count* left[i]

print(total)
