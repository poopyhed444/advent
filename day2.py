

# try:
# 	count =0
# 	while True:
# 		flag = False
# 		nums = [int(x) for x in input().split()]
# 		sortd = nums.copy()
# 		sorta = nums.copy()
# 		sortd.sort()
# 		sorta.sort(reverse = True)
# 		if (sortd == nums or sorta ==nums):
# 			for i in range(len(nums) -1):
# 				if (abs(nums[i+1] - nums[i]) <= 3 and abs(nums[i+1] - nums[i]) >=1 ):
# 					continue
# 				else: 
# 					flag = True
# 		else:
# 			flag = True
# 		if (flag == False):
# 			count += 1
		

# except EOFError:
# 	pass

# print(count)




try:
    count = 0
    while True:
        nums = [int(x) for x in input().split()]
        original_set = set(nums)
        valid_nums =[]
      
        for i in range(len(nums)):
            if (i == 0 or abs(nums[i] - nums[i-1]) <= 3 and abs(nums[i] - nums[i-1]) >= 1):
              valid_nums.append(i)
        if len(nums) - len(valid_nums) <= 1 and set(valid_nums) == original_set:
            count += 1

except EOFError:
    pass

print(count)
