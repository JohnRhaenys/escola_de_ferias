""" Removendo elemento da lista (outra forma) """

lista = [10, 20, 30, 40, 50]

print('Antes da remocao: ', lista)

# Remove o elemento na POSICAO e retorna o valor
valor_removido = lista.pop(0)

print('Valor removido: ', valor_removido)
print('Apos a remocao: ', lista)