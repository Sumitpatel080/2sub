from bot import Bot

Bot().run()
from telegram.ext import Updater, CommandHandler
from commands.admin import setchannel

# Initialize bot
updater = Updater("YOUR_BOT_TOKEN")
dispatcher = updater.dispatcher

# Register admin commands
dispatcher.add_handler(CommandHandler("setchannel", setchannel))

# Start the bot
updater.start_polling()
updater.idle()
