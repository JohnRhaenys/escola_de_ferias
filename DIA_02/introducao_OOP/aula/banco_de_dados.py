import os
import pickle


class BancoDeDados:

    # Constante estatica (tambem chamada de constante de classe)
    CAMINHO_ARQUIVO = os.path.join(os.getcwd(), 'series.pkl')

    def __init__(self):

        # Variavel de instancia
        self.dados = {}

    def salvar_dados(self):
        try:
            # Abrindo o arquivo em forma de escrita binaria
            with open(self.CAMINHO_ARQUIVO, 'wb') as file:
                pickle.dump(self.dados, file, pickle.HIGHEST_PROTOCOL)
            print('Dados salvos com sucesso!')
            return True
        except Exception as e:
            print('Erro ao salvar os dados')
            print(str(e))
            return False

    def carregar_dados(self):

        # Abrindo o arquivo em modo de leitura binario
        with open(self.CAMINHO_ARQUIVO, 'rb') as file:
            try:
                self.dados = pickle.load(file)
                return True
            except EOFError as e:
                print(str(e))
                return False

    def mostrar_tudo(self):
        if not self.dados:
            print('Dados vazios!')
        else:
            for nome, objeto_serie in self.dados.items():
                print(f'{nome}: {objeto_serie}')

    def buscar_serie(self, nome_da_serie):
        """
        Buscamos a serie com complexidade de O(1). Ultra rapido,
        independente da quantidade de dados
        """
        return self.dados.get(nome_da_serie)
