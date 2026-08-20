numbers = [10,45,23,89,12,67]

bigger = numbers[0]

for number in numbers:
    if number > bigger:
        bigger = number

print(bigger)