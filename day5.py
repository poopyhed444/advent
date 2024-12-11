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

def keep_swapping(nums, testlist):
    changed = True
    while changed:
        changed = False
        for i in range(len(nums) - 1):
            a = [nums[i], nums[i+1]]
            if a not in testlist and swap(a) in testlist:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                changed = True
    return nums

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
        if "," not in inputs:
            break
        nums = [int(x) for x in inputs.split(",")]
        testlist = []
        for i in range(len(nums)):
            for j in range(len(sigma)):
                if (nums[i] == sigma[j][0]):
                    testlist.append(sigma[j])
        original_nums = nums.copy()
        nums = keep_swapping(nums, testlist)
        
        if nums != original_nums:
            mid = nums[len(nums) // 2]
            mids.append(mid)

except EOFError:
    pass


print(sum(mids))
