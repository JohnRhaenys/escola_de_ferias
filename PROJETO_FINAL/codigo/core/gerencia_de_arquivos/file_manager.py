import os
import pickle

"""
Usado para gerenciar os arquivos do meu sistema
"""


def create_file(file_path):
    """
    Cria um arquivo no caminho especificado

    :param file_path: caminho onde o arquivo sera' criado
    """
    try:
        with open(file_path, 'wb') as file:
            pickle.dump({}, file, pickle.HIGHEST_PROTOCOL)
    except FileNotFoundError as e1:
        raise e1
    except Exception as e2:
        raise e2


def file_exists(file_path):
    """
    Verifica se um arquivo existe no caminho especificado

    :param file_path: caminho do arquivo que estou verificado
    :return: True se existe, False caso contrario
    """
    return os.path.isfile(file_path)
