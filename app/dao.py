import os

from typing import NoReturn, List

from .models import Produto, Categoria

from .util import File


class CategoriaDAO:

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        File.create(nome_do_arquivo)

    def create(self, categoria: Categoria) -> NoReturn:
        File.write(self.nome_do_arquivo, categoria)

    def read(self) -> List[Categoria]:
        lista_categorias_str = File.read(self.nome_do_arquivo).splitlines()
        return [Categoria(i[0], i[1]) for i in lista_categorias_str]

    def delete(self):
        pass

    def update(self):
        pass


class ProdutoDAO:

    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        File.create(nome_do_arquivo)

    def create(self, produto: Produto) -> NoReturn:
        File.write(self.nome_do_arquivo, produto)

    def read(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
