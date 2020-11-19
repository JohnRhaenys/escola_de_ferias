numeros = [0, 1, 2, 3]

tamanho = len(numeros)

primeiro = numeros[0]

"""
 FORMATO -> lista[inicio : fim] (exclusive)

 OBS: Se nenhum valor for passado como inicio ou fim, o Python considera 
 o inicio como a primeira posicao da lista e o fim como a ultima posicao da lista
"""

pedaco_1 = numeros[0:len(numeros)]
pedaco_2 = numeros[:]


print('Lista: ', numeros)
print('Primeiro: ', primeiro)
print('Pedaco 1: ', pedaco_1)
print('Pedaco 2: ', pedaco_2)
