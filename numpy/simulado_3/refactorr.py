# Converte uma lista de strings para floats, trocando 'N' por 0
def listaStrToFloat(l):
    for i in range(len(l)):
        l[i] = 0 if l[i] == 'N' else float(l[i])

# Calcula média ponderada e soma dos pesos com base na lista l e pesos p
def mediaPonderada(l, p):
    if len(l) != len(p):
        print('[mediaPonderada] Erro nos parâmetros.')
        exit()
    soma_ponderada = 0
    soma_pesos = 0
    for i in range(len(l)):
        if l[i] > 0:
            soma_ponderada += l[i] * p[i]
            soma_pesos += p[i]
    return soma_ponderada / soma_pesos, soma_pesos

# ======================
# ETAPA 1 – Ler arquivo notas.csv
# ======================

nome_notas = 'notas.csv'
try:
    with open(nome_notas) as arquivo:
        posicao_codigo_aluno = 0
        posicao_nome_aluno = 1
        posicao_codigo_curso = 2
        posicao_primeira_nota = 4

        alunos_por_curso = {}

        for linha in arquivo:
            campos = linha.strip().split(';')

            curso = campos[posicao_codigo_curso]
            dados_aluno = [campos[posicao_codigo_aluno], campos[posicao_nome_aluno]] + campos[posicao_primeira_nota:]

            if curso in alunos_por_curso:
                alunos_por_curso[curso].append(dados_aluno)
            else:
                alunos_por_curso[curso] = [dados_aluno]

except:
    print(f"Erro na abertura do arquivo {nome_notas}")
    exit()

# ======================
# ETAPA 2 – Ler arquivo pesos.csv
# ======================

nome_pesos = 'pesos.csv'
try:
    with open(nome_pesos) as arquivo_pesos:

        # ======================
        # ETAPA 3 – Processar curso por curso
        # ======================
        for curso in alunos_por_curso:

            # Reposiciona o cursor do arquivo para o início
            arquivo_pesos.seek(0)
            pesos = []

            # Busca linha correspondente ao curso
            for linha in arquivo_pesos:
                if linha.startswith(curso):
                    pesos = linha.strip().split(';')[1:]  # ignora o código do curso

            listaStrToFloat(pesos)

            alunos_do_curso = alunos_por_curso[curso]
            resultado_por_aluno = {}

            for dados in alunos_do_curso:
                nome = dados[1]
                notas = dados[2:]
                listaStrToFloat(notas)

                media, soma_pesos = mediaPonderada(notas, pesos)
                resultado_por_aluno[nome] = [dados[0], (media, soma_pesos)]

            # Ordena nomes dos alunos
            nomes_ordenados = sorted(resultado_por_aluno)

            # ======================
            # ETAPA 4 – Salvar arquivo por curso
            # ======================

            nome_saida = f'alunos_Curso_{curso}.csv'
            with open(nome_saida, mode='w') as arquivo_saida:
                for nome in nomes_ordenados:
                    codigo = resultado_por_aluno[nome][0]
                    media = resultado_por_aluno[nome][1][0]
                    pesos_utilizados = resultado_por_aluno[nome][1][1]
                    linha_saida = f"{nome};{codigo};{media:.3f};{pesos_utilizados}\n"
                    arquivo_saida.write(linha_saida)

except:
    print(f"Erro na abertura do arquivo {nome_pesos}")
    exit()

print("✅ Fim da execução.")
