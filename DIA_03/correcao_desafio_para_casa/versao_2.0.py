import os


def main():
    caminho_arquivo = os.path.join(os.getcwd(), 'cadastro_professores.txt')
    with open(caminho_arquivo) as arquivo:
        # A funcao arquivo.readlines() retorna uma lista, em que cada posicao
        # da lista eh uma linha do arquivo. Portanto, posso usar list comprehension aqui
        # Se ficou com dúvida, veja esses vídeos:
        #
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        # https://www.youtube.com/watch?v=3dt4OGnU5sM

        [enviar_email(email.strip('\n'), gerar_mensagem(get_nome(email))) for email in arquivo.readlines()]


def get_nome(email):
    nome, _ = email.strip().split('@')
    return nome


def gerar_mensagem(nome):
    mensagem = f"""
    Bom dia, {nome.capitalize()}!

    Gostaria de dar os meus parabéns a você. É um prazer enorme fazer parte
    dessa equipe de profissionais da PUC. Desejo-te muita saúde, paz e dinheiro!

    Atenciosamente, Carol.
    """
    return mensagem


def enviar_email(email, mensagem):
    print(f'Enviando email para {email}')
    print(f'Mensagem: {mensagem}')
    print('-=' * 50)


if __name__ == '__main__':
    main()
