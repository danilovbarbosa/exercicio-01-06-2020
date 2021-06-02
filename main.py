import os, sys

from app.dao import CategoriaDAO
from app.models import Categoria


def main():
    categoria = Categoria("nome teste", "nome descricao")
    
    nome_do_arquivo = os.getcwd() + "/" + "test.txt"
    
    categoriaDAO = CategoriaDAO(nome_do_arquivo)
    categoriaDAO.create(categoria.__str__())

    isExist = os.path.exists(nome_do_arquivo)
    print(isExist)
    
    assert isExist == False, f"O valor deveria ser True, porém foi {isExist}"

if __name__ == '__main__':    
    main()
    