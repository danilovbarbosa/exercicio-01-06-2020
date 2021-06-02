import os

from app.models import Produto, Categoria
from app.dao import ProdutoDAO

class TestProduto:
    
    def test_deve_criar_um_arquivo_com_uma_produto(self):
        categoria = Categoria("nome teste", "nome descricao")

        produto = Produto("nome teste", "nome descricao", 33, categoria.__str__())
        
        nome_do_arquivo = os.getcwd() + "/" + "test_produto.txt"
        
        produtoDAO = ProdutoDAO(nome_do_arquivo)
        produtoDAO.create(produto.__str__())

        isExist = os.path.exists(nome_do_arquivo)
        
        assert isExist is True, f"O valor deveria ser True, porém foi {isExist}"
    
    def test_deve_ler_o_arquivo_com_categorias(self):       
        nome_do_arquivo = os.getcwd() + "/" + "test_categoria.txt"
        
        categoriaDAO = CategoriaDAO(nome_do_arquivo)

        list_categorias = categoriaDAO.read()
        
        assert isinstance(list_categorias, list), f"O valor deveria ser [], porém foi {list_categorias}"