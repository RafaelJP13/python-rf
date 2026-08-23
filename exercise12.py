# Uma forma de contar quantas vezes um número aparece
numbers: list[int] = [10, 20, 10, 30, 20, 10, 40, 30, 20]

counter: dict[int, int] = {}

for number in numbers:

    found: bool = False

    for key in counter:

        if key == number:
            counter[key] += 1
            found = True
            break

    if found == False:
        counter[number] = 1

print(counter)

