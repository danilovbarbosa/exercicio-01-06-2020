import os

from typing import NoReturn, List

from .models import Produto, Categoria

from .util import File


class DAO:
    
    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


class CategoriaDAO(DAO):

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        File.create(nome_do_arquivo)

    def create(self, categoria: Categoria) -> None:
        File.write(self.nome_do_arquivo, categoria)

    def read(self) -> List[Categoria]:
        lista_str = File.read(self.nome_do_arquivo).splitlines()
        return [Categoria(i[0], i[1]) for i in lista_str]

    def delete(self, numero_da_linha: int) -> None:
        File.remove(self.nome_do_arquivo, numero_da_linha)

    def update(self):
        pass


class ProdutoDAO(DAO):

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        File.create(nome_do_arquivo)

    def create(self, produto: Produto) -> None:
        File.write(self.nome_do_arquivo, produto)

    def read(self) -> List[Produto]:
        lista_str = File.read(self.nome_do_arquivo).splitlines()
        return [Produto(i[0], i[1], i[2], i[3]) for i in lista_str]

    def delete(self, numero_da_linha: int) -> None:
        File.remove(self.nome_do_arquivo, numero_da_linha)

    def update(self):
        pass
