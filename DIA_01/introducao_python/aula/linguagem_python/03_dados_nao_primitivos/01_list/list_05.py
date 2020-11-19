numeros = [0, 1, 2, 3]

tamanho = len(numeros)

primeiro = numeros[0]


"""
 FORMATO -> lista[inicio : fim] (exclusive)

 OBS: Se nenhum valor for passado como inicio, o Python considera 
 o inicio como a primeira posicao da lista
"""


pedaco_1 = numeros[:1]
pedaco_2 = numeros[:2]
pedaco_3 = numeros[:3]
pedaco_4 = numeros[:4]

print('Lista: ', numeros)
print('Primeiro: ', primeiro)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
print('Pedaco 3: ', pedaco_3)
print('Pedaco 4: ', pedaco_4)

