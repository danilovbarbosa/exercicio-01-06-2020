from app.dao import CategoriaDAO

def main():
    categoria = CategoriaDAO("a.txt")
    categoria.create("vasdva")

if __name__ == '__main__':    
    main()
    