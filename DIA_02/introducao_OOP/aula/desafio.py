"""

Você foi contratado para desenvolver um sistema de pesquisa de séries de televisão de um site.

O dono do site quer que você crie um programa desktop (sem conexão com a internet) para
que o usuário pesquise informações offline sobre séries de televisão.

As informações importantes sobre as séries são:

1) Nome da série
2) Ano de lançamento
3) Avaliação

O dono do site quer que o usuário possa digitar o nome da série, e o sistema deve
recuperar as informações sobre a série e mostrar na tela para o usuário.


EXEMPLO DE ENTRADA DO USUARIO
##########################################################################
'Breaking Bad'
##########################################################################


SAIDA NA TELA
##########################################################################
# A série Breaking Bad foi lançada no ano 2012 e possui avaliação de 9.4
##########################################################################

O site é https://www.imdb.com/chart/toptv

"""
from DIA_02.introducao_OOP.aula.banco_de_dados import BancoDeDados
from DIA_02.introducao_OOP.aula.serie import Serie


def get_lista_de_series(caminho_arquivo_html):

    # Abrindo o arquivo HTML em modo leitura
    with open(caminho_arquivo_html, 'r') as file:

        title_tag = '<td class="titleColumn">'

        lista_de_series = []

        while True:

            linha = file.readline()

            if not linha:
                break

            if title_tag in linha:
                _ = file.readline()
                linha = file.readline()

                # Pegando o nome da serie
                nome = get_atributo(linha)

                # Pegando o ano da serie
                linha = file.readline()
                ano = get_atributo(linha)

                # Pulando duas linhas
                _ = file.readline()
                _ = file.readline()

                # Pegando a avalicao da serie
                linha = file.readline()
                avaliacao = get_atributo(linha)

                objeto_serie = Serie(nome, ano, avaliacao)
                lista_de_series.append(objeto_serie)

        return lista_de_series


def get_atributo(linha):
    inicio = linha.find('>')
    fim = linha.rfind('<')
    return linha[inicio + 1:fim]


def criar_tabela_hash(lista_de_series):
    """
    Criar uma tabela hash com os dados das series.
    Estamos fazendo isso porque precisamos acessar os dados
    de forma instantanea, ou seja, em complexidade O(1).
    Isso faz o programa ficar muito mais rapido!

    :param lista_de_series: lista de objetos 'Serie'

    :return: tabela hash (dicionario) com os dados das series

    A chave é o nome da serie e o valor é o objeto Série
    Podemos fazer isso porque o nome da serie é um identificador único,
    ou seja, nao existem duas series com o mesmo nome (tomara)!
    """
    tabela_hash = {}

    for serie in lista_de_series:
        nome = serie.nome
        tabela_hash[nome] = serie

    # return {serie.nome: serie for serie in lista_de_series}

    return tabela_hash


def main():
    banco_de_dados = BancoDeDados()

    caminho = '/home/john/PycharmProjects/escola_de_ferias/DIA_02/introducao_OOP/aula/series.html'
    lista_de_series = get_lista_de_series(caminho)

    tabela_hash = criar_tabela_hash(lista_de_series)
    banco_de_dados.dados = tabela_hash

    # Salvando os dados no HDD
    salvou = banco_de_dados.salvar_dados()
    if not salvou:
        return

    # Carregando os dados do HDD para a memoria RAM
    tudo_ok = banco_de_dados.carregar_dados()
    if tudo_ok:
        input_usuario = input('Digite o nome da série que está procurando: ')

        objeto_serie = banco_de_dados.buscar_serie(input_usuario)

        """
        'None' eh a mesma coisa que null no Java ou no C
        A palavra 'is' eh usada pra comparar se objetos sao iguais (referencia)
        ou seja, se um objeto esta' no mesmo endereco de memoria que outro
        """
        if objeto_serie is not None:
            print(objeto_serie)
        else:
            print(f'A serie "{input_usuario}" não está cadastrada no sistema.')


if __name__ == '__main__':
    main()
