# import re


# search_string = ""
# for i in range(6):
#     search_string += input()
# regex = "mul\(([1-9]*),([1-9]*)\)"

# matches = re.findall(regex, search_string)

# print(matches)
# sums =0
# for match in matches:
#     numbers =[]
#     for num in match:
#         numbers.append(int(num))
#     sums += (numbers[0] * numbers[1])
# print(sums)



import re


search_string = ""
for i in range(1):
    search_string += input()
regex = "mul\(([1-9]*),([1-9]*)\)|do(())|don'\t(())"
matches = re.finditer(regex, search_string)
total =0
# for match in matches:
#     print(match.group())
flag = False
for match in matches:
    if "mul" in match.group() and flag == False:
        sigma = match.group().split(",")
        print(sigma)
        
