import telegram.ext
import pandas_datareader as web

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update, context):
    update.message.reply_text("""
    Hello Welcome to Stock Price Bot!
    Use /help to see other commands.
    """)

def help(update, context):
    update.message.reply_text("""
    You can use the following commands:

    /start -> Welcome message
    /help -> This message
    /stock FB-> The current price of FB
    *You can add "-USD" for cryptocrrencies(ex:BTC-USD)
    
    """)

def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f"The current price of {ticker} is ${price:.2f}")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}.")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
