# Find the second largest number in a 

numbers = [10, 45, 23, 89, 12, 67, 34]

bigger = numbers[0]
secondBigger = numbers[0]

for number in numbers:
    if number > bigger:
        secondBigger = bigger
        bigger = number
    elif number > secondBigger:
        secondBigger = number

print(secondBigger)