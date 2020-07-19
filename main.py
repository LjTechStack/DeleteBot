# External import
import discord
import logging
# Local import
from helpers.main.keys import keys
import discordBotFunctions

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(name)s - %(levelname)s: %(message)s')
    # fileLogger = logging.FileHandler(filename='temp/log/log.log')
    # fileLogger.setLevel(logging.INFO)
    # fileFormatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s: %(message)s')
    # fileLogger.setFormatter(fileFormatter)

    # logging.getLogger('main').addHandler(fileLogger)
    logger = logging.getLogger('main')

    logger.info('application starting')
    client = discord.Client()
    discordBotFunctions.connect(client)
    logger.info('client running')
    client.run(keys.CLIENT_KEY)

