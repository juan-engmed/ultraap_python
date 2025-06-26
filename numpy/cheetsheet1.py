import numpy as np

# =============================
# 🧠 NumPy Cheatsheet - Prova
# =============================

# 1. LEITURA DE ARQUIVOS
# ----------------------
# np.loadtxt lê arquivos com dados numéricos (texto).
# Retorna um array NumPy com os valores do arquivo.
dados = np.loadtxt('arquivo.txt')  # Exemplo: matriz 2D com floats


# 2. .shape e .shape[0]
# ---------------------
# .shape mostra o formato (linhas, colunas) do array.
# .shape[0] retorna o número de linhas (ou elementos se for 1D).
a = np.array([[1, 2, 3], [4, 5, 6]])
print(f"shape: {a.shape}")     # (2, 3)
print(f"linhas: {a.shape[0]}") # 2
print(f"colunas: {a.shape[1]}")# 3


# 3. .reshape(n, 1)
# -----------------
# Transforma vetor 1D em matriz coluna.
v = np.array([10, 20, 30])
print(v.reshape(3, 1))  # [[10], [20], [30]]


# 4. .sort()
# ---------
# Ordena os elementos do array (in-place).
b = np.array([5, 2, 8])
b.sort()
print(f"Ordenado: {b}")  # [2 5 8]


# 5. np.concatenate()
# -------------------
# Junta arrays horizontalmente (axis=1) ou verticalmente (axis=0).
x = np.array([[1], [2]])
y = np.array([[10], [20]])
c = np.concatenate((x, y), axis=1)
print(f"Concatenado:\n{c}")  # [[ 1 10] [ 2 20]]


# 6. np.abs()
# -----------
# Valor absoluto dos elementos.
z = np.array([-4, 3, -2])
print(f"Valor absoluto: {np.abs(z)}")  # [4 3 2]


# 7. Verificar negativos com .any()
# ---------------------------------
arr = np.array([2, -5, 7])
tem_negativo = (arr < 0).any()
print(f"Contém negativos? {tem_negativo}")  # True


# 8. np.savetxt()
# ---------------
# Salva array numérico em arquivo com 6 casas decimais.
array_salvar = np.array([[1.234567], [8.9101112]])
np.savetxt('saida.txt', array_salvar, fmt='%.6f')  # Gera: 1.234567\n8.910111


# 9. np.savetxt() com strings (como 'null')
# -----------------------------------------
dados_null = np.array([["35.000000", "null", "null"], ["40.000000", "null", "null"]])
np.savetxt('saida.txt', dados_null, fmt='%s')  # Gera linhas com texto


# 10. np.full()
# -------------
# Cria matriz preenchida com valor constante.
nulos = np.full((3, 1), "null")
print(f"Matriz de null:\n{nulos}")


# 11. Escrita manual com f-strings
# --------------------------------
produtos = ['arroz', 'feijao']
precos = {'arroz': 5.99, 'feijao': 8.5}
with open('produtos.txt', 'w') as f:
    for p in produtos:
        linha = f"{p};{precos[p]:.2f}\n"
        f.write(linha)
# Gera:
# arroz;5.99
# feijao;8.50


# 12. Exemplo de saída combinada com valores + null
# --------------------------------------------------
numeros_validos = np.array([[10.0, 9.5, 0.5], [20.0, 19.7, 0.3], [30.0, 30.0, 0.0]])
faltando_info = np.array([["35.000000", "null", "null"], ["40.000000", "null", "null"]])

# Salva no mesmo arquivo
with open("saida.txt", 'w') as f:
    np.savetxt(f, numeros_validos, fmt='%.6f')
with open("saida.txt", 'a') as f:
    np.savetxt(f, faltando_info, fmt='%s')

# Conteúdo final de saida.txt:
# 10.000000 9.500000 0.500000
# 20.000000 19.700000 0.300000
# 30.000000 30.000000 0.000000
# 35.000000 null null
# 40.000000 null null


# 13. Tabela resumo comentada
# ----------------------------

# Função                         | Uso
# ------------------------------|-----------------------------
# np.loadtxt('arq.txt')         | Lê arquivo texto numérico
# np.savetxt('arq.txt', arr)    | Salva array em arquivo
# arr.shape                     | Retorna (linhas, colunas)
# arr.reshape(n, 1)             | Transforma vetor em matriz coluna
# arr.sort()                    | Ordena elementos in-place
# np.abs(arr)                   | Valor absoluto dos elementos
# (arr < 0).any()               | Verifica se há negativos
# np.concatenate((a,b), axis=1) | Junta arrays horizontalmente
# np.full((n,1), 'null')        | Matriz com 'null'
# open().write(...)             | Escrita personalizada linha por linha

print("✅ Cheatsheet finalizada. Boa prova!")
