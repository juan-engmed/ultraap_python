from collections import deque

def is_pessoa_vendedor(nome, grafo):
    return grafo[nome]['vendedor_de_mangas']

def vendedor_de_manga_pesquisa_em_largura(fila_de_pesquisa, grafo):
    verificados = set()
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if pessoa not in verificados:
            if is_pessoa_vendedor(pessoa, grafo):
                print(f'{pessoa} é vendedor de manga!')
                return pessoa
            else:
                fila_de_pesquisa += grafo[pessoa]['pessoas_conhecidas']
                verificados.add(pessoa)
    return None

def main():
    grafo = {
        'tom': {'pessoas_conhecidas': [], 'vendedor_de_mangas': True},
        'alice': {'pessoas_conhecidas': ['tom'], 'vendedor_de_mangas': False},
        'bob': {'pessoas_conhecidas': [], 'vendedor_de_mangas': False},
        'juan': {'pessoas_conhecidas': ['alice', 'bob'], 'vendedor_de_mangas': False}
    }

    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo['juan']['pessoas_conhecidas']

    result = vendedor_de_manga_pesquisa_em_largura(fila_de_pesquisa, grafo)
    if result:
        print(f'A pessoa vendedora mais próxima é: {result}')
    else:
        print(f'Não há vendedores próximos')

if __name__ == "__main__":
    main()

        

