import re


search_string = ""
for i in range(6):
    search_string += input()
regex = r"mul\((\d+),(\d+)\)"
matches = re.findall(regex, search_string)

print(matches)
sums =0
for match in matches:
    numbers =[]
    for num in match:
        numbers.append(int(num))
    sums += (numbers[0] * numbers[1])
print(sums)
