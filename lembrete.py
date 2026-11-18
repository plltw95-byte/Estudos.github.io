import os
import json
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

url = os.environ.get("DISCORD_WEBHOOK_LEMBRETES")
if not url:
    raise SystemExit("Faltou o segredo DISCORD_WEBHOOK_LEMBRETES no GitHub.")

agora = datetime.now(ZoneInfo("America/Sao_Paulo"))
arquivo = "lembretes_manha.txt" if agora.hour < 14 else "lembretes_noite.txt"

with open(arquivo, encoding="utf-8") as f:
    mensagens = [linha.strip() for linha in f if linha.strip()]

texto = mensagens[agora.timetuple().tm_yday % len(mensagens)]
mensagem = texto + " @everyone"

dados = json.dumps({
    "content": mensagem,
    "allowed_mentions": {"parse": ["everyone"]},
}).encode("utf-8")

pedido = urllib.request.Request(
    url,
    data=dados,
    headers={"Content-Type": "application/json", "User-Agent": "lembrete-estudo/1.0"},
)
urllib.request.urlopen(pedido)
print("Enviado:", mensagem)
