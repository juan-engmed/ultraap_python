"""
=======================================================
📄 CHEATSHEET 4.1 – CSV com NumPy + slicing + arquivos
Autor: você   |   Foco: slicing [:,1], open('w'), open('a')
=======================================================
"""

import numpy as np

# =======================================================
# 🔹 1. SLICING EM NUMPY – O QUE SIGNIFICA [:, 1], [:2], [1:]
# =======================================================

"""
A sintaxe geral de slicing é:
    array[linhas, colunas]

EXEMPLO:
"""
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 🧠 matriz[:, 0] → todas as linhas, coluna 0
print(matriz[:, 0])  # [10 40 70]

# 🧠 matriz[:, :2] → todas as linhas, colunas 0 e 1
print(matriz[:, :2])
# [[10 20]
#  [40 50]
#  [70 80]]

# 🧠 matriz[1:, :] → da linha 1 em diante, todas as colunas
print(matriz[1:, :])
# [[40 50 60]
#  [70 80 90]]

# 🧠 matriz[:2, 1:] → até a linha 1 (excluindo 2), colunas 1 e 2
print(matriz[:2, 1:])
# [[20 30]
#  [50 60]]

# 🧠 matriz[1, :] → só a linha 1 inteira
# 🧠 matriz[:, -1] → última coluna de todas as linhas


# =======================================================
# 🔹 2. ABRIR ARQUIVOS EM MODO 'w', 'a' e usar WITH
# =======================================================

"""
'w' = write (escreve do zero, apaga conteúdo anterior)
'a' = append (acrescenta no final sem apagar o que já tem)

'with open' é a forma segura e pythonic de abrir arquivos.
"""

# Exemplo 1 – modo 'w' (sobrescreve)
with open('produtos.csv', mode='w') as f:
    f.write("Produto,Preco\n")
    f.write("arroz,5.99\n")
    f.write("feijao,8.50\n")

# Exemplo 2 – modo 'a' (adiciona no final)
with open('produtos.csv', mode='a') as f:
    f.write("macarrao,6.40\n")


# =======================================================
# 🔹 3. USANDO SLICING EM CSV COM NUMPY
# =======================================================

dados = np.loadtxt('entrada.csv', delimiter=',', skiprows=1)

coluna1 = dados[:, 0]     # 1ª coluna (todos os valores)
duas_colunas = dados[:, :2]  # colunas 0 e 1
ultima_coluna = dados[:, -1]  # última

primeiras_linhas = dados[:3, :]  # 3 primeiras linhas

# Concatenar coluna1 + coluna2 + erro
erro = np.abs(dados[:, 0] - dados[:, 1]).reshape(-1, 1)
resultado = np.concatenate((dados[:, :2], erro), axis=1)

# Salvar com cabeçalho
np.savetxt('saida.csv', resultado, delimiter=',', fmt='%.2f',
           header='Valor1,Valor2,Erro', comments='')


# =======================================================
# 🔹 4. Mini visual da estrutura para lembrar
# =======================================================

"""
Suponha:
dados = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

dados[0, 1]   → 20
dados[:, 0]   → [10 40 70]
dados[1:, 2:] → [[60], [90]]
dados[:, :2]  → [[10 20], [40 50], [70 80]]
dados[-1, :]  → [70 80 90]
"""

# =======================================================
# 🔹 5. Funções rápidas para lembrar
# =======================================================

"""
📦 np.loadtxt('arquivo.csv', delimiter=',', skiprows=1)
💾 np.savetxt('saida.csv', array, delimiter=',', fmt='%.2f')

✂️ Slicing:
array[linha, coluna]
array[:, i]        → coluna i
array[i, :]        → linha i
array[:2, 1:]      → primeiras 2 linhas, colunas a partir da 2
array[-1, :]       → última linha

🧪 open():
with open('x.csv', 'w') as f → sobrescreve
with open('x.csv', 'a') as f → acrescenta
f.write(f"{produto},{preco:.2f}\\n")

🧠 axis:
np.concatenate((a, b), axis=0) → empilha
np.concatenate((a, b), axis=1) → cola lado a lado
"""

print("✅ Cheatsheet 4.1 (slicing + arquivos + csv) pronta!")
