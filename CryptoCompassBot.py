from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging,telegram
import emoji 
from rules import st


# Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# All required command handlers
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Dear User, \n\nI'm the *CryptoCompass* bot. I can help you with the following.\n\n1. How to Invest ?\n2. Current Deals\n3. Survey: Which ICO would you like on CryptoCompass\n4. Submit your ICO\n5. Rules", parse_mode='Markdown')
    

def help(bot, update):
    """Send a message when the command /help is issued."""
    user = update.message.from_user.first_name
    update.message.reply_text('Hello {} looking for Help! \n/start - To start the bot \n/help - To get list of all commands \n/currentdeals - To learn about investment \n/bonus - To get the bonus deals\n/submit- To submit an ICO \n/survey - To do a survey on which ICO you want on cryptocompass \n/rules - To view group rules and regulations'.format(user))


def currentdeals(bot, update):
    """How to Invest ? (Current Deals)"""
    bot.send_message(chat_id=update.message.chat_id, text="Become a member on [CryptoCompass](http://www.crypto-compass.io/)", parse_mode='Markdown')
    
def bonus(bot, update):
    """ICO extra bonus"""
    bot.send_message(chat_id=update.message.chat_id, text="You need to login to [CryptoCompass](http://www.crypto-compass.io/) to see the bonus.", parse_mode='Markdown')

def submit(bot, update):
    """Submit your ICO"""
    bot.send_message(chat_id=update.message.chat_id, text="Please apply at the end of the homepage of [CryptoCompass](http://www.crypto-compass.io/)\n\nIn stage 1, our partner Blockpulse, a French compnay dedicated to ICO audit and investors relation will contact you if you have been selected to continue into stage 2 (due diligence) [Blockpulse](www.blockpulse.eu)", parse_mode='Markdown')

def survey(bot, update):
    """Survey Part"""
    bot.send_message(chat_id=update.message.chat_id, text="Fill this [form](http://goo.gl/forms/sMqxDE8RLW2Qs1ab2) to let us know which ICO you would like to see on our platform.", parse_mode='Markdown')

def about(bot,update):
    update.message.reply_text('This bot is made and hosted by @ashveservice \n Visit us at http://www.ashveservices.com)')

def rules(bot,update):
    update.message.reply_text(st)
    
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():

    # Event handler and pass token
    updater = Updater(token='619567191:AAH_JriBOC4Klqp7YYZqR-6_syOKdyfVZBY')

    # Dispatcher to register handlers
    dp = updater.dispatcher

    # Different commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("currentdeals", currentdeals))
    dp.add_handler(CommandHandler("bonus", bonus))
    dp.add_handler(CommandHandler("submit", submit))
    dp.add_handler(CommandHandler("survey", survey))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("Rules", rules))

    # On non command message, echo the same message
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()



     
