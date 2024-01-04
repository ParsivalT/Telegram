from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
from classes import CoinGeckoAPI, dolar
import os
import datetime
import requests



load_dotenv()

TOKEN = os.getenv("TOKEN")


import datetime

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def bitcoin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    API = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
    print("Entrei na API")
    try:
        print("Cheguei")
        mensagem = []
        
        # Supondo que 'atualizado_em' seja obtido de algum lugar
        atualizado_em = datetime.datetime.now().timestamp()
        data_hora = datetime.datetime.fromtimestamp(atualizado_em).strftime('%x %X')

        preco, _ = API.consulta_preco(id_moeda='bitcoin')
        preço_dolar, variacao = dolar()
        
        mensagem.append(f'*Últimas Atualizações*')
        mensagem.append(f'*Cotação do Dólar:* \n\t*Preço*: R$ {preço_dolar:.2f}' \
                        f'\n\t*Variação de:* {variacao}%')
        mensagem.append(f'*Cotação do Bitcoin*: \n\t*Preço*: R$ {preco:,.2f}' \
                        f'\n\t*Horário*: {data_hora}\n\t')
        
        for men in mensagem:
            print(men)
            await update.message.reply_markdown(text=men)

    except ConnectionError as err:
        print("DEU ERRO")
        await update.message.reply_text(text=str(err))


async def coffer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try: 
        data = requests.get("https://coffee.alexflipnote.dev/random.json").json()
        file_url = data['file']
    
        await update.message.reply_photo(photo=file_url)

    except:
        await update.message.reply_text("Estou com Problemas Para cessar a api")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bit", bitcoin))
app.add_handler(CommandHandler("coffer", coffer))
app.run_polling()

