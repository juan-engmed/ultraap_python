import pika
import json
import requests
from csv_writer import salvar_csv

BOT_TOKEN = "8108038958:AAFIXuzzohheg81AutXup7OvYaDtjvfUTwE"
CHAT_ID = 7126966128

def send_telegram_message(mensagem):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensagem}
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ Telegram OK")
    else:
        print(f"❌ Telegram ERRO: {response.text}")

# Filas
NORMAL_ALERT_QUEUE = 'normal_alert_queue'
ATTENTION_ALERT_QUEUE = 'attention_alert_queue'
CRITICAL_ALERT_QUEUE = 'critical_alert_queue'
filas = [NORMAL_ALERT_QUEUE, ATTENTION_ALERT_QUEUE, CRITICAL_ALERT_QUEUE]

# Conexão
credentials = pika.PlainCredentials("user", "password")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()
for fila in filas:
    channel.queue_declare(queue=fila, durable=True)

# Callback
def callback(ch, method, properties, body):
    try:
        mensagem = json.loads(body)
        alerta = mensagem.get("nivel_alerta", "")
        justificativa = mensagem.get("resumo_analise", "")
        paciente_id = mensagem.get("paciente_id", "?")

        print(f"\n📥 Fila [{method.routing_key}] - Paciente {paciente_id}")

        if alerta in ["Atencao", "Alerta Critico"]:
            send_telegram_message(f"🚨 [{alerta}] Paciente {paciente_id}\n{justificativa}")

        salvar_csv(mensagem)

    except Exception as e:
        print(f"❌ Erro no callback: {e}")

for fila in filas:
    channel.basic_consume(queue=fila, on_message_callback=callback, auto_ack=True)

print("🚀 Aguardando mensagens...")
channel.start_consuming()
