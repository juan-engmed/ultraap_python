# 1.1 A pesquisa em largura determina se há um caminho de A para A
# 1.2 Se existir um caminho, a pesquisa em largura fornecerá o menor caminho

# 2.1 Grafos não Direcionados não contêm setas, logo a relação é nos dois sentidos
# 2.2 Grafos Direcionados Rama -> Adit  "Rame deve dinheiro a Adit"

# 3.1 Os grafos se utilizam das mecânicas de Filas para realizar as pesquisa
# 3.2 Filas são do tipo FIFO (First In, First Out), logo isso permite buscarmos dados em 1º grau, depois em 2º grau e assim por diante.
# 3.3 Também permite verificar os dados na ordem que foram adicionados a lista de pesquisa, portanto esta lista é uma FILA, caso contrário, não obteremos o caminho Mínimo
# 3.4 Cada vez que um dado for verificado é necessário adiciona-lo a conjunto de verificados, para evitarmos loop de sempre verificarmos novamente

#Implementação Básica
from collections import deque

def is_pessoa_vendedor(pessoa):
    return pessoa[-1] == 'm'

def vendedor_de_manga_pesquisa_em_largura(fila_de_pesquisa, grafo):
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if is_pessoa_vendedor(pessoa):
            print(f'{pessoa} é vendedor de maga!')
            return pessoa
        else:
            fila_de_pesquisa += grafo.get(pessoa)
    return None

def main():
    fila_de_pesquisa = deque()

    #Grafos em Python são Dict
    grafo = {}
    grafo['juan'] = ['alice', 'bob', 'claire']

    grafo.update({'alice': ['peggy'],
                'bob': ['anuj', 'peggy'],
                'claire': ['thom', 'jonny'],
                'anuj': [],
                'peggy': [],
                'thom': [],
                'jonny': []})

    fila_de_pesquisa += grafo.get('juan')


    result = vendedor_de_manga_pesquisa_em_largura(fila_de_pesquisa, grafo)
    if result:
        print(f'A pessoa vendedora mais próxima é: {result}')
    else:
        print(f'Não há vendedores próximos')

    
if __name__ == "__main__":
    main()

        

