from typing import NoReturn, List

from .models import Produto, Categoria

from .util import File


class CategoriaDAO:
    
    def __init__(self, nome_do_arquivo):
        self.nome_do_arquivo = nome_do_arquivo
        File.criar(nome_do_arquivo)

    def create(self, categoria: Categoria) -> NoReturn:
        File.escrever(self.nome_do_arquivo, categoria)


    def read(self) -> List[Categoria]:
        pass

    def delete(self):
        pass
    
    def update(self):
        pass    
    
    
class ProdutoDAO:
    def create(self):
        pass

    def read(self):
        pass

    def delete(self):
        pass
    
    def update(self):
        pass    
    