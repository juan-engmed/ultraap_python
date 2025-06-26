import numpy as np

def erro(array1, array2):
    """
    Calcula o erro absoluto entre dois arrays NumPy.
    Ambos os arrays devem ter o mesmo tamanho.
    Exemplo: erro([10, 20], [8, 18]) => [2, 2]
    """
    return np.abs(array1 - array2)  # np.abs() retorna o valor absoluto de cada elemento


def verificar_negativo(array):
    """
    Verifica se o array contém algum valor negativo.
    Retorna True se houver ao menos um valor negativo.
    """
    return (array < 0).any()  # (array < 0) gera um array booleano; .any() verifica se algum é True


def carregar_dados(nome_arquivo):
    """
    Tenta carregar um arquivo texto com dados numéricos usando np.loadtxt.
    Em caso de erro (arquivo não existe ou está mal formatado), exibe mensagem e encerra o programa.
    """
    try:
        dados = np.loadtxt(nome_arquivo)
        return dados
    except:
        print(f'Erro no acesso ao arquivo {nome_arquivo}')
        exit()


def salvar_saida(nome_arquivo, matriz_dados, matriz_nulos=None):
    """
    Salva a matriz de dados formatada no arquivo de saída.
    Se houver matriz_nulos, ela será adicionada ao final do arquivo.
    """
    try:
        with open(nome_arquivo, 'w') as f:
            np.savetxt(f, matriz_dados, fmt='%.6f')  # salva os dados principais com 6 casas decimais

        if matriz_nulos is not None:
            with open(nome_arquivo, 'a') as f:
                np.savetxt(f, matriz_nulos, fmt='%s')  # salva os dados nulos como string ("null")
    except:
        print(f'Erro na escrita do arquivo {nome_arquivo}')
        exit()


def main():
    # Carrega os arquivos com os dados
    tabela = carregar_dados('tabela.txt')
    info = carregar_dados('info.txt')

    # Verifica se o arquivo info.txt contém valores negativos
    if verificar_negativo(info):
        print("Erro: o arquivo info.txt contém valores negativos.")

    # Seleciona a coluna de interesse (por índice)
    indice_coluna = 2
    coluna = tabela[:, indice_coluna]

    # Ordena os dados das duas listas
    coluna.sort()
    info.sort()

    # Conta quantos elementos tem cada lista
    total_coluna = coluna.shape[0]
    total_info = info.shape[0]

    # Variável de controle para casos em que info tem menos dados que coluna
    completar_com_null = False

    if total_info < total_coluna:
        completar_com_null = True
        n = total_info

        # Calcula o erro entre os n primeiros elementos
        erro_array = erro(coluna[:n], info)

        # Gera a lista de valores restantes da coluna (que não têm pares em info)
        qtd_restante = total_coluna - n
        valores_restantes = [f"{coluna[i]:.6f}" for i in range(n, total_coluna)]

        # Cria a matriz com os valores restantes e 'null'
        saida_null = np.concatenate(
            (
                np.array(valores_restantes).reshape(qtd_restante, 1),
                np.full((qtd_restante, 1), "null"),
                np.full((qtd_restante, 1), "null")
            ),
            axis=1
        )
    else:
        n = total_coluna
        erro_array = erro(coluna, info[:n])
        saida_null = None  # nada a completar

    # Recorta os dados até n para montar a matriz principal
    coluna_final = coluna[:n].reshape(n, 1)
    info_final = info[:n].reshape(n, 1)
    erro_final = erro_array.reshape(n, 1)

    # Junta os dados em uma matriz 2D com 3 colunas
    saida = np.concatenate((coluna_final, info_final, erro_final), axis=1)

    # Salva os dados em 'saida.txt'
    salvar_saida('saida.txt', saida, saida_null)

    print("Fim da execução.")

# Ponto de entrada
if __name__ == "__main__":
    main()
