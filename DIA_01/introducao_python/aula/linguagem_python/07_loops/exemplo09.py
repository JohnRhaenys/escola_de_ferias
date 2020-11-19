nomes = ['MAX', 'FELIPE', 'THELDO']

nome = input('Insira o seu nome: ')

if nome in nomes:
    print(f'Olá, professor {nome}!')
else:
    print(f'Olá, aluno {nome}!')