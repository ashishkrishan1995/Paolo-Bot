from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging,telegram
import emoji 
from rules import st


# Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# All required command handlers
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Dear User, \n\nI'm the *CryptoCompass* bot. I can help you with the following.\n\n1. How to Invest?\n2. Current Deal\n3. Survey: Which ICO would you like on CryptoCompass\n4. Submit your ICO.", parse_mode='Markdown')
    

def help(bot, update):
    """Send a message when the command /help is issued."""
    user = update.message.from_user.first_name
    update.message.reply_text('Hello {} looking for Help! \n/start - To start the bot \n/help - To get list of all commands \n/invest - To learn abour investment \n/bonus - To get the bonous deals\n/submit- To submit the ICO \n/survey - To do a survery on which ICO you want on cryptocompass \n/rules - TO view group rules and regulations'.format(user))


def invest(bot, update):
    """How to Invest ?"""
    bot.send_message(chat_id=update.message.chat_id, text="Become a member on [CryptoCompass](http://www.crypto-compass.io/)", parse_mode='Markdown')
    
def bonus(bot, update):
    """ICO extra bonus"""
    bot.send_message(chat_id=update.message.chat_id, text="You need to login to [CryptoCompass](http://www.crypto-compass.io/) to see the bonus.", parse_mode='Markdown')

def submit(bot, update):
    """Submit your ICO"""
    update.message.reply_text('')

def survey(bot, update):
    """Survey Part"""
    update.message.reply_text('Which ICO would you like on CryptoCompass ?')

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
    updater = Updater(token='501606167:AAFSvnmbvbISIL09P4_slr8SsSO-VfFVHYU')

    # Dispatcher to register handlers
    dp = updater.dispatcher

    # Different commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("invest", invest))
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



     
