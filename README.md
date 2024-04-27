# Telegram Username to User ID Converter Bot

Brief description of your bot.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

To use the Telegram Username to User ID Converter Bot, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git.
    ```bash
    git clone https://github.com/ATOUIYakoub/telegram-username-to-user-id-bot.git
    ```
2. **Install Dependencies**: Navigate to the project directory and install the required dependencies.
    ```bash
    cd telegram-username-to-user-id-bot
    pip install -r requirements.txt
    ```
3. **Replace Telegram Token**: Open the `boot.py` file and replace the `YOUR_TELEGRAM_TOKEN_HERE` placeholder with your own Telegram bot token. You can obtain a token by creating a new bot using [BotFather](https://core.telegram.org/bots#botfather).

    ```python
    # config.py

    # Replace 'YOUR_TELEGRAM_TOKEN_HERE' with your own Telegram bot token
    TOKEN = 'YOUR_TELEGRAM_TOKEN_HERE'
    ```

4. **Run the Bot**: Start the bot by running the `boot.py` file.
    ```bash
    python boot.py
    ```

That's it! The bot should now be up and running, ready to convert Telegram usernames to user IDs.

## Usage

To use the Telegram Username to User ID Converter Bot, follow these steps:

1. **Start the Bot**: Start a conversation with the bot by searching for it on Telegram and typing "/Start".
2. **Get User ID**: Once the bot welcomes you, send your username to the bot. It will then reply with your user ID.

That's it! The bot will handle the rest.

## Contributing

We welcome contributions to improve the Telegram Username to User ID Converter Bot.

Thank you for contributing!
