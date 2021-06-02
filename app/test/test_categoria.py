import os

from app.models import Categoria
from app.dao import CategoriaDAO

class TestCategoria:
    
    def test_deve_criar_um_arquivo(self):
        categoria = Categoria("nome teste", "nome descricao")
        
        nome_do_arquivo = os.getcwd() + "/" + "test_categoria.txt"
        
        categoriaDAO = CategoriaDAO(nome_do_arquivo)
        categoriaDAO.create(categoria.__str__())

        isExist = os.path.exists(nome_do_arquivo)
        
        assert isExist is True, f"O valor deveria ser True, porém foi {isExist}"