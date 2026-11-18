import os
import json
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

url = os.environ.get("DISCORD_WEBHOOK")
if not url:
    raise SystemExit("Faltou o segredo DISCORD_WEBHOOK no GitHub.")

with open("frases.txt", encoding="utf-8") as f:
    frases = [linha.strip() for linha in f if linha.strip()]

hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))
frase = frases[hoje.timetuple().tm_yday % len(frases)]

mensagem = "☀️ **Bom dia! Frase do dia:**\n> " + frase + "\n\nBons estudos! 📚🔥"

dados = json.dumps({"content": mensagem}).encode("utf-8")
pedido = urllib.request.Request(
    url,
    data=dados,
    headers={"Content-Type": "application/json", "User-Agent": "frase-diaria/1.0"},
)
urllib.request.urlopen(pedido)
print("Enviado:", frase)
