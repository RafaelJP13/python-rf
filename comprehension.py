numbers = [number for number in range(1, 6)]


type: list[str] = [
    "par" if number % 2 == 0 else "impar"
    for number in numbers

]

print(type)