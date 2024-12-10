# from re import L


# sigma = []

# while True:
#     try:
#         line = input()
#         if "|" not in line:
#             break
#         sigma.append([int(x) for x in line.split("|")])
#     except EOFError:
#         break

# print(sigma)
# mids = []
# try: 
#     while True:
#         inputs = input()
#         testlist = []
#         if "," in inputs:
#             nums = [int(x) for x in inputs.split(",")]
#         else: 
#             break
#         for i in range(len(nums)):
#             for j in range(len(sigma)):
#                 if (nums[i] == sigma[j][0]):
#                     testlist.append(sigma[j])
#         flag = False
#         for i in range(len(nums) -1):
#                 a = []
#                 a.append(nums[i])
#                 a.append(nums[i+1])
#                 if (a in testlist):
#                     continue
#                 else:
#                     flag = True
                    
#         if (flag == False):
#             mids.append(nums[int((len(nums) - 1) / 2)])
        
# except EOFError:
#     pass

# print(sum(mids))



def swap(skibidi):
	a = skibidi[0]
	skibidi[0] = skibidi[1]
	skibidi[1] = a
	return skibidi
sigma = []

while True:
    try:
        line = input()
        if "|" not in line:
            break
        sigma.append([int(x) for x in line.split("|")])
    except EOFError:
        break

print(sigma)
mids = []
try: 
    while True:
        inputs = input()
        testlist = []
        if "," in inputs:
            nums = [int(x) for x in inputs.split(",")]
        else: 
            break
        for i in range(len(nums)):
            for j in range(len(sigma)):
                if (nums[i] == sigma[j][0]):
                    testlist.append(sigma[j])
        flag = False
        for i in range(len(nums) - 1):
            a = []
            a.append(nums[i])
            a.append(nums[i+1])
            if (a in testlist):
                continue
            else:
                flag = True
                skibidi = swap(a)
                if (skibidi in testlist):
                    print(nums)
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    print(nums)
        if (flag == True):
            print(nums[int((len(nums) - 1) / 2)])
            mids.append(nums[int((len(nums) - 1) / 2)])

except EOFError:
    pass



print(sum(mids))
