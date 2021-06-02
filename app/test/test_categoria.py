from app.dao import CategoriaDAO
import os, sys
sys.path.append(os.getcwd())

from app.dao import CategoriaDAO

class TestCategoria:
    
    def test_deve_criar_um_arquivo():
        resultado = CategoriaDAO("teste.txt")
        
        assert resultado == 1, f"O valor deveria ser 1, porém foi {resultado}"