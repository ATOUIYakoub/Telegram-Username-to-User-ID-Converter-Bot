from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
import logging
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6548214352:AAEYkydS1WJ855rv3rvCmy9XCuko-7WCMRA'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Send me your username, and I will return your user ID.')

# Define a function to handle incoming messages
async def echo(update: Update, context: CallbackContext) -> None:
    # Get the username from the message
    username = update.message.text
    # Get the user ID based on the username
    user_id = get_user_id(username)
    if user_id:
        # Reply with the username and user ID
        await update.message.reply_text(f'Your username is {username}, your user ID is {user_id}.')
    else:
        await update.message.reply_text('Username not found.')

def get_user_id(username):
    # Make a request to the Telegram Bot API to get information about the updates
    response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    data = response.json()
    if data['ok']:
        # Search for the user ID corresponding to the provided username
        for update in data['result']:
            if 'message' in update and 'from' in update['message'] and 'username' in update['message']['from']:
                if update['message']['from']['username'] == username:
                    return update['message']['from']['id']
    return None

def main() -> None:
    # Create an Application instance
    application = Application.builder().token(TOKEN).build()
    
    # Add command handler to the application
    application.add_handler(CommandHandler("start", start))

    # Add message handler to the application
    # Make sure that the echo function is being called for non-command messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Enable logging for debugging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Run the bot until you press Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
