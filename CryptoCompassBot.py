from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


# Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

#All required command handlers
def start(bot, update):
    update.message.reply_text("Dear User, \nI'm the CryptoCompass bot. I can help you with the following.\n\n1. How to Invest?\n2. Current Deal\n3. Survey: Which ICO would you like on CryptoCompass\n4. Submit your ICO.")

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def invest(bot, update):
    """How to Invest ?"""
    update.message.reply_text('')

def submit(bot, update):
    """Submit your ICO"""
    update.message.reply_text('')

def submit(bot, update):
    """Survey Part"""
    update.message.reply_text('Which ICO would you like on CryptoCompass ?')

    
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
    dp.add_handler(CommandHandler("submit", submit))
    dp.add_handler(CommandHandler("survey", survey))

    # On non command message, echo the same message
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()



     
