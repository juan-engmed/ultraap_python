import os
import csv

CSV_PATH = "dados_recebidos.csv"

# Cria o cabeçalho do CSV se ele ainda não existir
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            "paciente_id",
            "idade",
            "sexo",
            "estado_permanente",
            "classificacao_final_id",
            "classificacao_final",
            "justificativa",
            "bpms_analisados"
        ])

def salvar_csv(mensagem):
    try:
        dados_paciente = mensagem.get("dados_paciente", {})

        paciente_id = mensagem.get("paciente_id")
        idade = dados_paciente.get("idade")
        sexo = dados_paciente.get("sexo")
        estado_permanente = dados_paciente.get("estado")
        classificacao_final_id = mensagem.get("nivel_alerta_id")
        classificacao_final = mensagem.get("nivel_alerta")
        justificativa = mensagem.get("resumo_analise")
        bpms_analisados = mensagem.get("bpms_analisados")

        with open(CSV_PATH, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                paciente_id,
                idade,
                sexo,
                estado_permanente,
                classificacao_final_id,
                classificacao_final,
                justificativa,
                str(bpms_analisados)
            ])
        print("📝 CSV atualizado")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {e}")
