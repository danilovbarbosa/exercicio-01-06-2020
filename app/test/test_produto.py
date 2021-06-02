import os

from app.models import Produto, Categoria
from app.dao import ProdutoDAO


class TestProduto:

    def test_deve_criar_um_arquivo_com_uma_produto(self):
        nome_do_arquivo = os.getcwd() + "/" + "test_produto.txt"

        categoria = Categoria("nome teste", "nome descricao")

        produto = Produto("nome teste", "nome descricao", 33, categoria.__str__())
        
        produtoDAO = ProdutoDAO(nome_do_arquivo)
        produtoDAO.create(produto.__str__())

        isExist = os.path.exists(nome_do_arquivo)
        
        assert isExist is True, f"O valor deveria ser True, porém foi {isExist}"
    
    def test_deve_ler_o_arquivo_com_produtos(self):
        nome_do_arquivo = os.getcwd() + "/" + "test_produto.txt"
        produtoDAO = ProdutoDAO(nome_do_arquivo)
        
        list_produtos = produtoDAO.read()
        
        assert isinstance(list_produtos, list), f"O valor deveria ser [], porém foi {list_produtos}"
        
    def test_deve_remover_uma_linha_do_arquivo_com_produtos(self):       
        nome_do_arquivo = os.getcwd() + "/" + "test_produto.txt"
        
        produtoDAO = ProdutoDAO(nome_do_arquivo)
        tamanho_anteior = len(produtoDAO.read())

        produtoDAO.delete(0)
        tamanho_atual = len(produtoDAO.read())

        
        assert tamanho_anteior > tamanho_atual, f"O valor anterior, igual a {tamanho_anteior}, deveria ser maior, porém foi {tamanho_atual}"
