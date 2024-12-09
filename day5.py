from re import L


sigma = []
for i in range(21):
    sigma.append([int(x) for x in input().split("|")])

print(sigma)
mids = []
try: 
    # while True:
    for i in range(6):
        testlist = []
        nums = [int(x) for x in input().split(",")]
        for i in range(len(nums)):
            for j in range(len(sigma)):
                if (nums[i] == sigma[j][0]):
                    testlist.append(sigma[j])
                    print(testlist)
        flag = False
        for i in range(len(nums) -1):
                a = []
                a.append(nums[i])
                a.append(nums[i+1])
                print(a)
                if (a in testlist):
                    continue
                else:
                    flag = True
                    
        if (flag == True):
            mids.append(nums[int((len(nums) - 1) / 2)])
        
except EOFError:
    pass

print(sum(mids))
