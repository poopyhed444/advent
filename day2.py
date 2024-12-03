

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


def check(nums):
	for i in range(len(nums) -1):
			if (abs(nums[i+1] - nums[i]) <= 3 and abs(nums[i+1] - nums[i]) >=1 ):
				continue
			else:
				return False
	if ((nums == sorted(nums) or nums == sorted(nums, reverse= True))) :
		return True
	else: 
		return False

try:
	count =0
	while True:
		nums = [int(x) for x in input().split()]
		if (check(nums)):
			count+= 1
		else :
			flag = False
			for j in range(len(nums)):
				duplicate = nums.copy()
				duplicate.pop(j)
				if (check(duplicate)):
					flag = True
					break
				else:
					continue

			if (flag == True):
				count+= 1




except EOFError:
	pass

print(count)


