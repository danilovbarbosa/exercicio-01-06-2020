from pathlib import Path
import io


class Arquivo:
    
    @staticmethod
    def create(nome_do_arquivo):
        '''
        
        '''
        if not Path(nome_do_arquivo).exists():
            Path(nome_do_arquivo)

    @staticmethod
    def count_lines(nome_do_arquivo):
        try:
            arquivo = open(nome_do_arquivo, 'r')
            quantidade_de_linhas = len(arquivo.readlines())
            arquivo.close()

            return quantidade_de_linhas
        except FileNotFoundError:
            return 0

    @staticmethod
    def write(nome_do_arquivo, linha):
        '''
        >>> nome = "teste"
        >>> write(nome)
        '''

        quantidade_atual_de_linhas = Arquivo.count_lines(nome_do_arquivo)
        arquivo = open(nome_do_arquivo, 'a')
        try:
            arquivo.write(str(quantidade_atual_de_linhas) + ', ' + linha + '\n')

            return arquivo 

        except io.UnsupportedOperation:
            arquivo.write("0, " + linha + '\n')

            return arquivo 

        finally:
            arquivo.close()

    @staticmethod
    def read(nome_do_arquivo):
        '''
        >>> nome = "teste"
        >>> write(nome, "teste")
        >>> read(nome)
        teste
        '''
        arquivo = Path(nome_do_arquivo)
        return arquivo.read_text()
    
    @staticmethod
    def remove():
        return 0    