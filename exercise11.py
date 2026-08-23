a = 0
b = 1
result = a

for i in range(1,6):
    print(result)
    result = a + b
    a = b
    b = result
