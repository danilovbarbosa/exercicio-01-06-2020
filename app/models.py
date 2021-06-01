class Produto:
    
    def __init__(self, nome:str, descricao:str, valor:str, categoria: Categoria):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        self.__categoria = categoria
        
    @property
    def get_nome(self):
        return self.__nome
    
    @property
    def get_descricao(self):
        return self.__descricao

    @property
    def get_valor(self):
        return self.__valor


class Categoria:
    
    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao
