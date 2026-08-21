numbers = [10,20,30,40]

# Adiciona ao final da list
numbers.append(50)

# Adiciona multiplos elementos ao final da list
numbers.extend([60,80])

# Adiciona um elemento em uma posição específica
numbers.insert(0, 5)

# Remove a primeira ocorrência de determinado valor
numbers.remove(20)

# Remove o último elemento e retorna-o
removed_values = numbers.pop()

# Remove o elemento com base no index passado e retorna-o
another_removed_values = numbers.pop(1) #10

# Limpa todos elementos
# numbers.clear()

# Descobre o índice da primeira ocorrência do valor
position = numbers.index(30)

# Conta quantas vezes um valor aparece
count = numbers.count(30)

# Ordena lista
numbers.sort()

#Ordenar descrescente
numbers.sort(reverse=True)

# Cria cópia da lista eliminando a caracteristica de apontar para o mesmo endereço da memória
new_numbers = numbers.copy()

