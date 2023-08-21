# Chat_Id 1512304430

from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot, dolar, LOG
from time import sleep
import schedule


API = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
BOT = TelegramBot(token='5550528443:AAGgtgrN4j8sdppddbqE1gnyIvExz2sJUrQ', chat_id=1512304430)

def bot_telegram():

   
    if API.ping():
        
        preco, atualizado_em = API.consulta_preco(id_moeda='bitcoin')

        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = list()

        preço_dolar, variacao = dolar()

        mensagem.append(f'*Ultimas Atualizações*')
        mensagem.append(f'*Cotação do Dolar:* \n\t*Preço*: R$ {preço_dolar:.2f}' \
                    f'\n\t*Variação de:* {variacao}%')
        mensagem.append(f'*Cotação do Bitcoin*: \n\t*Preço*: R$ {preco:,.2f}' \
                    f'\n\t*Horario*: {data_hora}\n\t')

        for mensagens in mensagem:
            BOT.envia_mensagem(texto_markdown=mensagens)

        LOG.info("Mensagem enviada!")
        
    else:
        LOG.warning('Api offline, Tente denovo mais tarde!')


schedule.every(5).seconds.do(bot_telegram)

while True:
    schedule.run_pending()
    sleep(1)
