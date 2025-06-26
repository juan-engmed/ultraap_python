import numpy as np

# ==========================
# 1. LEITURA DE ARQUIVO COM TRATAMENTO DE ERRO
# ==========================

def carregar_arquivo(nome):
    """
    Tenta carregar um arquivo de texto com números usando NumPy.
    Em caso de erro (arquivo não existe ou está mal formatado), imprime mensagem.
    """
    try:
        dados = np.loadtxt(nome)
    except Exception as e:
        print(f"Erro ao abrir o arquivo '{nome}': {e}")
        return None
    else:
        print(f"Arquivo '{nome}' carregado com sucesso.")
        return dados

# Exemplo:
dados = carregar_arquivo('exemplo.txt')


# ==========================
# 2. SALVAR ARQUIVO COM TRATAMENTO DE ERRO
# ==========================

def salvar_arquivo(nome, array, fmt='%.6f'):
    """
    Tenta salvar um array NumPy em um arquivo texto.
    """
    try:
        with open(nome, 'w') as f:
            np.savetxt(f, array, fmt=fmt)
    except Exception as e:
        print(f"Erro ao salvar no arquivo '{nome}': {e}")
    else:
        print(f"Arquivo '{nome}' salvo com sucesso.")

# Exemplo:
array = np.array([[1.234567], [8.910111]])
salvar_arquivo('saida.txt', array)


# ==========================
# 3. np.concatenate – CONCEITO CLARO
# ==========================

"""
np.concatenate() serve para juntar dois arrays.
O parâmetro axis define o “lado” da junção:
→ axis=0: junta por baixo (empilha linhas)
→ axis=1: junta lado a lado (colunas)

MAS: as dimensões que **não são o axis** precisam bater!

📌 DICA:
- axis=0 → número de colunas precisa ser igual
- axis=1 → número de linhas precisa ser igual
"""

# EXEMPLO 1: axis=0 (empilhar)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
res = np.concatenate((a, b), axis=0)
print(f"axis=0 (empilhar):\n{res}")
# [[1 2]
#  [3 4]
#  [5 6]]

# EXEMPLO 2: axis=1 (lado a lado)
x = np.array([[1], [2], [3]])
y = np.array([[10], [20], [30]])
res2 = np.concatenate((x, y), axis=1)
print(f"axis=1 (colunas):\n{res2}")
# [[ 1 10]
#  [ 2 20]
#  [ 3 30]]


# ==========================
# 4. reshape – TRANSFORMAR VETOR EM MATRIZ
# ==========================

v = np.array([10, 20, 30])
v_reshape = v.reshape(3, 1)
print(f"reshape:\n{v_reshape}")
# [[10]
#  [20]
#  [30]]


# ==========================
# 5. abs e erro absoluto
# ==========================

def erro_absoluto(a1, a2):
    return np.abs(a1 - a2)

# Exemplo:
a = np.array([10, 20, 30])
b = np.array([8, 22, 29])
print(f"Erro absoluto: {erro_absoluto(a, b)}")
# [2 2 1]


# ==========================
# 6. Verificar se array tem negativo
# ==========================

arr = np.array([1, -5, 3])
print(f"Tem negativo? {(arr < 0).any()}")  # True


# ==========================
# 7. Salvar dados com 'null' (mistura string + float)
# ==========================

dados = np.array([
    ["10.0", "9.5", "0.5"],
    ["20.0", "null", "null"]
])
np.savetxt("saida_null.txt", dados, fmt='%s')


# ==========================
# 8. Criar matriz com valor fixo (np.full)
# ==========================

print(np.full((3, 1), "null"))
# [['null']
#  ['null']
#  ['null']]


# ==========================
# 9. sort – Ordena vetor
# ==========================

vetor = np.array([3, 1, 4])
vetor.sort()
print(f"Ordenado: {vetor}")  # [1 3 4]


# ==========================
# 10. shape e size
# ==========================

matriz = np.array([[1, 2], [3, 4], [5, 6]])
print(f"shape: {matriz.shape}")  # (3, 2) → 3 linhas, 2 colunas
print(f"size: {matriz.size}")    # 6 elementos totais


# ==========================
# 11. Escrita personalizada com f-string
# ==========================

produtos = ['arroz', 'feijao']
precos = {'arroz': 5.99, 'feijao': 8.50}
with open('produtos.txt', 'w') as f:
    for p in produtos:
        f.write(f"{p};{precos[p]:.2f}\n")
# Gera:
# arroz;5.99
# feijao;8.50


# ==========================
# 12. Tabela resumo das funções
# ==========================

"""
🔹 FUNÇÃO            | USO PRINCIPAL
---------------------|--------------------------
np.loadtxt           | Lê arquivo numérico
np.savetxt           | Salva array numérico ou string
np.abs               | Valor absoluto
np.concatenate       | Junta arrays (axis=0 ou 1)
np.reshape           | Transforma vetor em matriz coluna
np.full              | Cria matriz com valor constante
arr.sort()           | Ordena array inplace
(arr < 0).any()      | Verifica se há negativos
open().write(...)    | Escrita linha por linha personalizada
"""

print("✅ Cheatsheet Versão 2 pronta para prova!")
