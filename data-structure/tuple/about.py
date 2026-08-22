numbers: tuple[int, ...] = (10, 20, 30, 40)
user = ("Rafael", 27, "Python Specialist")
position = ("-23.987322", "-46.394737")
rgb = (255, 255, 255)

# Tuplas sem parênteses
others_numbers = 10,20,30

# Conta quantas vezes um valor aparece
times_appeared = numbers.count(20)

# Encontra a posição de um valor
value_position = numbers.index(20)

# unpackaging
name, age, role = user
