numbers = [10,20,30,40]

# Adiciona ao final da list
numbers.append(50)

# Adiciona multiplos elementos ao final da list
numbers.extend([60,70,80])

# Adiciona um elemento em uma posição específica
numbers.insert(0, 5)

# Remove a primeira ocorrência de determinado valor
numbers.remove(20)

# Remove o último elemento e retorna-o
removedValue = numbers.pop()

# Remove o elemento com base no index passado e retorna-o
anotherRemovedValue = numbers.pop(1) #10
