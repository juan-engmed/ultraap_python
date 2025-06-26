"""
====================================================
🧠 CHEATSHEET – VERSÃO 3.1 (Pythonic + NumPy + List + Dict)
Autor: você 😉   |   Guia definitivo para prova
====================================================
"""

import numpy as np

# ============================================
# 🔹 0. PYTHON NATIVO: list, dict, tuple, str
# ============================================

# 📌 LISTAS
lista = [1, 2, 3]
lista.append(4)
lista.extend([5, 6])
lista.insert(2, 9)     # insere na posição 2
lista.remove(2)        # remove o valor 2
ultimo = lista.pop()   # remove o último elemento
indice = lista.index(3) if 3 in lista else -1
existe = 4 in lista    # True

# List comprehension
quadrados = [x**2 for x in lista if x % 2 == 0]

# 📌 TUPLAS (imutáveis, com desempacotamento)
coordenada = (3, 4)
x, y = coordenada

# 📌 STRINGS
s = "Python"
print(s.lower(), s.upper(), s.startswith("Py"))

# 📌 DICIONÁRIOS
p = {'arroz': 5.99, 'feijão': 8.50}
p['macarrão'] = 6.40
valor = p.get('arroz', 0)
chaves = list(p.keys())
valores = list(p.values())
pares = list(p.items())

# Iteração com f-string
for produto, preco in p.items():
    print(f"{produto.capitalize():<10}: R$ {preco:.2f}")

# Deletar
del p['arroz']

# Dict comprehension
dobro = {k: v*2 for k, v in p.items()}


# ============================================
# 🔹 1. ARQUIVOS COM ERRO TRATADO
# ============================================

def carregar_float_txt(nome):
    try:
        return np.loadtxt(nome)
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome}' não encontrado.")
    except ValueError as e:
        print(f"❌ Erro de conteúdo: {e}")
    return None

def salvar_array_txt(nome, arr, fmt='%.6f'):
    try:
        with open(nome, 'w') as f:
            np.savetxt(f, arr, fmt=fmt)
    except Exception as e:
        print(f"❌ Erro ao salvar '{nome}': {e}")
    else:
        print(f"✅ Arquivo '{nome}' salvo.")


# ============================================
# 🔹 2. NUMPY CONCEITOS ESSENCIAIS
# ============================================

# Criando arrays
v = np.array([1, 2, 3])
z = np.zeros((2, 2))
r = np.random.rand(3)         # entre 0 e 1
i = np.arange(1, 6)           # [1 2 3 4 5]
idn = np.identity(3)          # matriz identidade

# Propriedades
v.shape
v.size
v.dtype

# Métodos úteis
v.sort()
v.reshape(-1, 1)
np.abs(v)
(v < 0).any()
np.full((3, 1), 'null')

# Concatenar arrays
a = np.array([[1], [2]])
b = np.array([[10], [20]])

# axis = 0 → empilhar (linhas)
print(np.concatenate((a, b), axis=0))
# [[ 1]
#  [ 2]
#  [10]
#  [20]]

# axis = 1 → lado a lado (colunas)
print(np.concatenate((a, b), axis=1))
# [[ 1 10]
#  [ 2 20]]


# ============================================
# 🔹 3. EXEMPLO COMPLETO: cálculo + saída
# ============================================

def exemplo_completo(col_idx=2):
    tabela = carregar_float_txt('tabela.txt')
    info = carregar_float_txt('info.txt')
    if tabela is None or info is None:
        return

    col = tabela[:, col_idx]
    col.sort()
    info.sort()

    n = min(len(col), len(info))
    erro = np.abs(col[:n] - info[:n])
    matriz_ok = np.column_stack((col[:n], info[:n], erro))

    salvar_array_txt('saida.txt', matriz_ok)

    if len(col) > len(info):
        faltantes = col[n:]
        nulls = np.column_stack((
            faltantes,
            np.full(faltantes.shape, 'null'),
            np.full(faltantes.shape, 'null')
        ))
        with open('saida.txt', 'a') as f:
            np.savetxt(f, nulls, fmt='%s')


# ============================================
# 🔹 4. RESUMO RÁPIDO: funções úteis para lembrar
# ============================================

"""
🧰 PYTHON BUILTIN
-----------------
len(), sum(), sorted(), min(), max(), round()
enumerate(), zip(), map(), filter(), any(), all()
dict.get(), list.append(), list.pop(), del dict[key]

🧮 NUMPY
--------
np.array, np.loadtxt, np.savetxt
arr.shape, arr.size, arr.dtype
arr.sort(), arr.reshape()
np.concatenate(), np.full()
np.abs(), (arr < 0).any()

📁 ARQUIVOS
----------
with open(...) as f:
    f.write(f"{variavel}\n")

💡 axis:
- axis=0 → empilha (linhas aumentam)
- axis=1 → cola lado a lado (colunas aumentam)
"""

print("✅ Cheatsheet V3.1 carregada com sucesso!")
