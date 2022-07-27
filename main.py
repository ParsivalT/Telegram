# bot do telegram para monitorar a cotacao de criptos
# version: 0.0.1

from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot 
from time import sleep
import locale
import config

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token=config.token, chat_id=config.chat_id)

while True:

    if api.ping():
        print('\nAPI online!')
        print(f'Horario: {datetime.now().ctime()}')
        preco, atualizado_em = api.consulta_preco(id_moeda='bitcoin')
        print('Consulta realizada com sucesso!')

        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < 113_500:
            mensagem = f'*Cotacao do Ethereum*: \n\t*Preco*: {locale.currency(preco, grouping=True)}' \
                       f'\n\t*Horario*: {data_hora}\n\t*Motivo*: Valor menor que o minimo'

        elif preco > 114_000:
            mensagem = f'*Cotacao do Ethereum*: \n\t*Preco*: {locale.currency(preco, grouping=True)}' \
                       f'\n\t*Horario*: {data_hora}\n\t*Motivo*: Valor maior que o maximo'

        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)

        print('='*30)
    else:
        print('Api offline, Tente denovo mais tarde!')

    sleep(300)
