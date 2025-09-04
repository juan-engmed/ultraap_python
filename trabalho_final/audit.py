import pandas as pd

# === Arquivos de entrada ===
ARQUIVO_ORIGINAL = "log_auditoria_classificacao.csv"
ARQUIVO_RECEBIDO = "dados_recebidos.csv"

# === Carrega os CSVs com codificação adequada ===
original_df = pd.read_csv(ARQUIVO_ORIGINAL, encoding="utf-8-sig")
recebido_df = pd.read_csv(ARQUIVO_RECEBIDO)

# Garante que paciente_id seja string para evitar falhas na comparação
original_df["paciente_id"] = original_df["paciente_id"].astype(str)
recebido_df["paciente_id"] = recebido_df["paciente_id"].astype(str)

# Define paciente_id como índice
original_df.set_index("paciente_id", inplace=True)
recebido_df.set_index("paciente_id", inplace=True)

# Identifica os IDs envolvidos
ids_orig = set(original_df.index)
ids_rec = set(recebido_df.index)

encontrados = ids_orig & ids_rec
faltando = ids_orig - ids_rec
extras = ids_rec - ids_orig

# === Seção 1: Resumo por tipo de alerta ===
resumo_alertas = (
    original_df
    .groupby("classificacao_final")
    .size()
    .reset_index(name="enviados")
    .set_index("classificacao_final")
)

recebidos_ok = original_df.loc[list(encontrados)]
resumo_recebidos = (
    recebidos_ok
    .groupby("classificacao_final")
    .size()
    .reset_index(name="recebidos")
    .set_index("classificacao_final")
)

# Junta os dois resumos
resumo_final = resumo_alertas.join(resumo_recebidos, how="left").fillna(0).astype(int)
resumo_final["percentual_recebido"] = (resumo_final["recebidos"] / resumo_final["enviados"] * 100).round(1)

# === Seção 2: Comparação por paciente ===
detalhes = []

for pid in sorted(encontrados):
    orig = original_df.loc[pid].to_dict()
    rec = recebido_df.loc[pid].to_dict()

    if orig == rec:
        detalhes.append({
            "paciente_id": pid,
            "status": "OK",
            "classificacao": orig["classificacao_final"],
            "detalhes": "100% igual"
        })
    else:
        diffs = []
        for col in original_df.columns:
            if col in rec and orig.get(col) != rec.get(col):
                diffs.append(f"{col}: '{orig.get(col)}' vs '{rec.get(col)}'")
        detalhes.append({
            "paciente_id": pid,
            "status": "DIFERENTE",
            "classificacao": orig["classificacao_final"],
            "detalhes": "; ".join(diffs)
        })

# Pacientes que estavam no original mas não foram recebidos
for pid in sorted(faltando):
    orig = original_df.loc[pid]
    detalhes.append({
        "paciente_id": pid,
        "status": "NÃO RECEBIDO",
        "classificacao": orig["classificacao_final"],
        "detalhes": "Paciente não chegou nas filas"
    })

# Pacientes que chegaram, mas não estavam no original
for pid in sorted(extras):
    rec = recebido_df.loc[pid]
    detalhes.append({
        "paciente_id": pid,
        "status": "EXTRA",
        "classificacao": rec["classificacao_final"],
        "detalhes": "Recebido, mas não enviado originalmente"
    })

# === Salva os arquivos de relatório ===
resumo_final.to_csv("resumo_alertas.csv")
pd.DataFrame(detalhes).to_csv("relatorio_auditoria.csv", index=False)

# === Mostra na tela ===
print("📊 Resumo de alertas enviados e recebidos:\n")
print(resumo_final)
print("\n✅ Detalhamento salvo em 'relatorio_auditoria.csv'")
