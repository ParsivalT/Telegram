# Importando as classes e funções necessárias
from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot, dolar, LOG  
from time import sleep
import schedule
from dotenv import load_dotenv
import os

load_dotenv()  # Carregando as variáveis de ambiente do arquivo .env

# Criando uma instância da classe CoinGeckoAPI com a URL base da API
API = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')

# Criando uma instância da classe TelegramBot com base nas variáveis de ambiente
BOT = TelegramBot(token=os.environ.get('TOKEN'), chat_id=os.environ.get('CHAT'))

def bot_telegram():
    if API.ping():  
        # Verificando se a API do CoinGecko está respondendo
        # Obtendo a cotação e o horário de atualização do Bitcoin
        preco, atualizado_em = API.consulta_preco(id_moeda='bitcoin')

        # Convertendo o timestamp para um formato de data e hora legível
        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = []  # Lista para armazenar as mensagens a serem enviadas

        # Obtendo informações sobre a cotação do dólar e variação
        preço_dolar, variacao = dolar()

        # Adicionando informações sobre a cotação do dólar e Bitcoin à lista de mensagens
        mensagem.append(f'*Últimas Atualizações*')
        mensagem.append(f'*Cotação do Dólar:* \n\t*Preço*: R$ {preço_dolar:.2f}' \
                        f'\n\t*Variação de:* {variacao}%')
        mensagem.append(f'*Cotação do Bitcoin*: \n\t*Preço*: R$ {preco:,.2f}' \
                        f'\n\t*Horário*: {data_hora}\n\t')

        # Enviando as mensagens formatadas para o chat do Telegram
        for mensagem in mensagens:
            BOT.envia_mensagem(texto_markdown=mensagem)

        LOG.info("Mensagem enviada!")  # Registrando no log que a mensagem foi enviada com sucesso
    else:
        LOG.warning('API offline, tente novamente mais tarde!')  # Avisando que a API está offline

# Agendando a execução da função bot_telegram a cada 4 horas
schedule.every(4).hours.do(bot_telegram)

# Loop principal que verifica e executa as tarefas agendadas
while True:
    schedule.run_pending()  # Executando tarefas agendadas
    sleep(1)  # Pausa de 1 segundo para evitar consumo excessivo de recursos
