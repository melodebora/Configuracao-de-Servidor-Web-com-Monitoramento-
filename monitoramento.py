import requests
import logging
import os
from datetime import datetime

# Configuração do log
log_file = "/var/log/monitoramento.log"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Webhook do Discord
webhook_url = "https://discord.com/api/webhooks/seu-link-de-webhooks-aqui"  # Seu webhook do Discord

# URL do site a ser monitorado
site_url = "http://ip-do-seu-site-aqui/"  # O site que pretendo monitorar

def enviar_notificacao_discord(mensagem):
    payload = {"content": mensagem}
    requests.post(webhook_url, json=payload)

def verificar_site():
    try:
        resposta = requests.get(site_url)
        if resposta.status_code == 200:
            logging.info(f"Site {site_url} está disponível.")
        else:
            logging.warning(f"Site {site_url} retornou o status {resposta.status_code}.")
            enviar_notificacao_discord(f"🚨 Alerta! O site {site_url} está com problemas. Status: {resposta.status_code}")
    except requests.RequestException as e:
        logging.error(f"Erro ao tentar acessar o site: {e}")
        enviar_notificacao_discord(f"🚨 Alerta! O site {site_url} não está respondendo. Erro: {e}")

if __name__ == "__main__":
    verificar_site()
