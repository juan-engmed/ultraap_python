import numpy as np

dados = np.loadtxt('numpy/datasets/apples_ts.csv', delimiter=',', usecols=np.arange(1, 88, 1))
print(dados)
ano_inicial = 2002
ano_final = 2102
print(np.arange(ano_inicial, ano_final + 1, 4))

lista = [1,2,3,4]

array = np.array(lista)

print(lista)
print(array)

#Obtendo dimensões
dados.ndim
#Visualizando numero de linhas e colunas
dados.shape #(linhas, colunas)

#Transposição
dados_transposto = dados.T

#array[linhas, colunas]
#: → seleciona tudo

#a:b → pega da coluna a até antes da b
#intencao_compras = clientes[:, 4:6]