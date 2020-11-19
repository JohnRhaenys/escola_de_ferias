"""
Fazer um programa para realizar uma busca em uma pagina HTML.

A url é 'http://www.savewalterwhite.com/'

Buscar o nome 'Walter White', presente no início da página e imprimir na tela

DICA: O código fonte da página já está disponível na variável 'source_code',
então é só buscar o conteúdo dentro das tags na string da página.

OBS: Precisa instalar o pacote 'requests'
-> pip install requests
"""


def get_html_page(url='http://www.savewalterwhite.com/'):
    import requests
    response = requests.get(url)
    return response.text if response.ok else None


def main():
    source_code = get_html_page()
    print(source_code)


if __name__ == '__main__':
    main()
