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
for i in range(6):
    search_string += input()
regex = r"mul\((\d*),(\d*)\)|do\(\)|don't\(\)"
matches = re.finditer(regex, search_string)
total =0
flag = False
for match in matches:
    if "don't()" in match.group():
        flag = True
    if "do()" in match.group():
        flag = False
    if "mul" in match.group() and flag == False:
        sigma = match.group()
        # print(sigma)
        pattern = re.compile("(\d*),(\d*)")
        sus = pattern.findall(sigma)
        for i in sus:
            num1 = int(i[0])
            num2 = int(i[1])
            total += (num1 * num2)
            

print(total)
