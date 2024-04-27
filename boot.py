from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import logging
import requests

# Replace 'YOUR_TELEGRAM_TOKEN_HERE' with your actual bot token
TOKEN = 'YOUR_TELEGRAM_TOKEN_HERE'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Send me your username, and I will return your user ID.')

async def echo(update: Update, context: CallbackContext) -> None:
    username = update.message.text
    user_id = get_user_id(username)
    if user_id:
        await update.message.reply_text(f'Your username is {username}, your user ID is {user_id}.')
    else:
        await update.message.reply_text('Username not found.')

def get_user_id(username):
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = response.json()
    if data['ok']:
        for update in data['result']:
            if 'message' in update and 'from' in update['message'] and 'username' in update['message']['from']:
                if update['message']['from']['username'] == username:
                    return update['message']['from']['id']
    return None

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
