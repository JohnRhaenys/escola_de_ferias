numeros = [0, 1, 2, 3]

tamanho = len(numeros)

primeiro = numeros[0]

"""
 FORMATO -> lista[inicio : fim] (exclusive)
"""

pedaco_1 = numeros[0:4]
pedaco_2 = numeros[1:4]
pedaco_3 = numeros[2:4]
pedaco_4 = numeros[3:4]

print('Lista: ', numeros)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)

print()

pedaco_1 = numeros[0:]
pedaco_2 = numeros[1:]
pedaco_3 = numeros[2:]
pedaco_4 = numeros[3:]

print('Lista: ', numeros)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)