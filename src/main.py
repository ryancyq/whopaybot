from settings import EnvSettings
from database import Database
from telegrambot import TelegramBot
import logging


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    settings = EnvSettings()
    db = Database(
        settings.DB_HOST,
        settings.DB_NAME,
        settings.DB_PORT,
        settings.DB_USER,
        settings.DB_PASS
    )
    bot = TelegramBot(settings.TOKEN,
                      settings.APP_NAME,
                      settings.PORT,
                      db,
                      settings.IS_PROD)