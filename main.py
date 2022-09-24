# Chat_Id 1512304430
from datetime import datetime
from classes import CoinGeckoAPI, TelegramBot, dolar
from time import sleep
from rich.console import Console
import schedule



console = Console()
API = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
BOT = TelegramBot(token='5550528443:AAHD2RjvRdzvwRJIOlR0ieOUCgYBPxJUoeQ', chat_id=1512304430)

def bot_telegram():

    with console.status("[green]Processando... [/]") as status:

        if API.ping():
            console.log("[blue]API online[/]")
            preco, atualizado_em = API.consulta_preco(id_moeda='bitcoin')
        

            data_hora = datetime.fromtimestamp(atualizado_em).strftime('%x %X')
            mensagem = list()

            console.log("[blue]Consultando cotação dolar!![/]")
            preço_dolar, variacao = dolar()

            mensagem.append(f'*Ultimas Atualizações*')
            mensagem.append(f'*Cotação do Dolar:* \n\t*Preço*: R$ {preço_dolar:.2f}' \
                        f'\n\t*Variação de:* {variacao}%')
            mensagem.append(f'*Cotação do Bitcoin*: \n\t*Preço*: R$ {preco:,.2f}' \
                        f'\n\t*Horario*: {data_hora}\n\t')

            for mensagens in mensagem:
                BOT.envia_mensagem(texto_markdown=mensagens)

            console.log("[blue]mensagem enviada com sucesso![/]")
            
            
        else:
            print('Api offline, Tente denovo mais tarde!')


schedule.every(5).minutes.do(bot_telegram)

while True:
    schedule.run_pending()
    sleep(1)