from datetime import datetime


antes = datetime.now().microsecond
lista = list()
print('Valor: ', lista)
print('Tipo: ', type(lista))
print('Mais lerdo')
depois = datetime.now().microsecond
print(depois - antes)


print()


antes = datetime.now().microsecond
lista_2 = []
print('Valor falso: ', lista_2)
print('Tipo: ', type(lista_2))
print('Mais rapido')
depois = datetime.now().microsecond
print(depois - antes)

