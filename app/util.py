from pathlib import Path

import io

from typing import TextIO


class File:

    @staticmethod
    def create(nome_do_arquivo: str) -> int:
        '''
        Deve criar um novo arquivo com o nome indicado no argumento: 
        nome_do_arquivo.
        '''

        if not Path(nome_do_arquivo).exists():
            Path(nome_do_arquivo)
            return 1
        return 0

    @staticmethod
    def count_lines(nome_do_arquivo: str) -> int:
        '''
        Deve ler um arquivo para contar a quantidade de linhas e retornar o 
        valor.
        
        >>> count_lines()
        0
        '''
        
        try:
            arquivo = open(nome_do_arquivo, 'r')
            quantidade_de_linhas = len(arquivo.readlines())
            arquivo.close()

            return quantidade_de_linhas
        
        except FileNotFoundError as e:
            print(e)
            return 0

    @staticmethod
    def write(nome_do_arquivo: str, linha: object) -> TextIO:
        '''
        Deve escrever o argumento linha no arquivo com o nome definido no 
        argumento: nome_do_arquivo.
        
        >>> nome = "teste"
        >>> write(nome)
        '''

        quantidade_atual_de_linhas = File.count_lines(nome_do_arquivo)
        arquivo = open(nome_do_arquivo, 'a')
        try:
            arquivo.write(
                str(quantidade_atual_de_linhas) + ', ' + str(linha) + '\n'
            )

            return arquivo 

        except io.UnsupportedOperation:
            arquivo.write("0, " + str(linha) + '\n')

            return arquivo 

        finally:
            arquivo.close()

    @staticmethod
    def read(nome_do_arquivo: str) -> str:
        '''
        >>> nome = "teste"
        >>> write(nome, "teste")
        >>> read(nome)
        teste
        '''
        arquivo = Path(nome_do_arquivo)
        return arquivo.read_text()

    @staticmethod
    def remove(nome_do_arquivo: str, numero_da_linha: int) -> None:
        '''
        Deve remover a linha indicada no argumento numero_da_linha no arquivo 
        com o nome definido no argumento: nome_do_arquivo.
        
        >>> nome = "teste"
        >>> remove(nome, 0)
        '''
        
        with open(nome_do_arquivo, "r") as f:
            lines = f.readlines()
            
        with open(nome_do_arquivo, "w") as f:
            for line in lines:
                if not str(numero_da_linha) in line.strip("\n"):
                    f.write(line)
