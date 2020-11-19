"""
A secretária, Carol, do curso de Ciência da Computação, deseja enviar uma mensagem de Feliz
Aniverśario a alguns os professores do departamento, que coincidentemente, fazem aniversário no mesmo dia.

São incluídos, também, professores dos cursos de sistemas de informação e de jogos.

A mensagem possui a seguinte estrutura:

    Bom dia, <nome_do_professor>!

    Gostaria de dar os meus parabéns a você. É um prazer enorme fazer parte
    dessa equipe de profissionais da PUC. Desejo-te muita saúde, paz e dinheiro!

    Atenciosamente, Carol.


A única coisa que ela possui é um arquivo "cadastro_professores.txt".
Infelizmente, os nomes dos professores não estão presentes no arquivo. Cada linha do arquivo possui
apenas o email do(a) professor(a).

Porém, para a sorte da secretária, o email é composto da seguinte forma:

<nome_do_professor>@gmail.com

Mesmo assim, se ela for mandar email por email, manualmente, vai levar o dia inteiro
para realizar a tarefa.

Ajude a Carol a enviar os emails de forma correta e rápida.

OBS: Obviamente nao precisa enviar um email (ate' porque os emails sao fake). Só
precisa printar na tela a mensagem correta com o nome de cada professor com a primeira
letra maiuscula

DICA: Usar a funcao 'capitalize()' da classe string to Python.

Amanha, no comeco da aula, vou corrigir este exercicio.

Divirta-se!
"""
import os


def main():
    caminho_arquivo = os.path.join(os.getcwd(), 'cadastro_professores.txt')
    with open(caminho_arquivo) as arquivo:
        for email in arquivo:
            nome = get_nome(email)
            mensagem = gerar_mensagem(nome)
            enviar_email(email, mensagem)


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
