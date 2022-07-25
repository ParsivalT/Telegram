# Chat_Id 1512304430
from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot 
from time import sleep


api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='5550528443:AAHD2RjvRdzvwRJIOlR0ieOUCgYBPxJUoeQ', chat_id=1512304430)

while True:
    if api.ping():
        print('API online!')
        preco, atualizado_em = api.consulta_preco(id_moeda='ethereum')
        print('Consulta realizada com sucesso!')

        data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
        mensagem = None

        if preco < 8000:
            mensagem = f'*Cotacao do Ethereum*: \n\t*Preco*: R$ {preco}' \
                       f'\n\t*Horario*: {data_hora}\n\t*Motivo*: Valor menor que o minimo'

        elif preco > 8000:
            mensagem = f'*Cotacao do Ethereum*: \n\t*Preco*: R$ {preco}' \
                       f'\n\t*Horario*: {data_hora}\n\t*Motivo*: Valor maior que o maximo'


        if mensagem:
            bot.envia_mensagem(texto_markdown=mensagem)

    else:
        print('Api offline, Tente denovo mais tarde!')


    sleep(60)
