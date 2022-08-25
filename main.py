# Chat_Id 1512304430
from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot, dolar
from time import sleep


api = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
bot = TelegramBot(token='5550528443:AAHD2RjvRdzvwRJIOlR0ieOUCgYBPxJUoeQ', chat_id=1512304430)


if api.ping():
    print('API online!')
    preco, atualizado_em = api.consulta_preco(id_moeda='bitcoin')
    print('Consulta realizada com sucesso!')

    data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
    mensagem = list()
    dolar = dolar()

    mensagem.append(f'*Ultimas Atualizações*')
    mensagem.append(f'*Cotação do Dolar:* \n\t*Preço*: R$ {dolar[0]:.2f}' \
                f'\n\t*Variação de:* {dolar[1]}%')
    mensagem.append(f'*Cotação do Ethereum*: \n\t*Preço*: R$ {preco:,.2f}' \
                f'\n\t*Horario*: {data_hora}\n\t')

    for mensagens in mensagem:
        bot.envia_mensagem(texto_markdown=mensagens)

    print("Menssagens Enviadas Com Sucesso!")
    
else:
    print('Api offline, Tente denovo mais tarde!')


