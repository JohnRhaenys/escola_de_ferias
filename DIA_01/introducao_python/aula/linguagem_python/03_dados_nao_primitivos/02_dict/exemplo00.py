from datetime import datetime


antes = datetime.now().microsecond
dicionario = dict()
print('Valor: ', dicionario)
print('Tipo: ', type(dicionario))
print('Mais lerdo')
depois = datetime.now().microsecond
print(depois - antes)


print()


antes = datetime.now().microsecond
dicionario2 = {}
print('Valor: ', dicionario2)
print('Tipo: ', type(dicionario2))
print('Mais rapido')
depois = datetime.now().microsecond
print(depois - antes)
