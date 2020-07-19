import logging

from command_handler import command_handler


def connect(client):
    logging.basicConfig(level=logging.INFO,
                        format='%(name)s - %(levelname)s: %(message)s')
    logger = logging.getLogger('discordBotFunctions')

    @client.event
    async def on_ready():
        logger.info('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            #delete logic not need, doesn't make sense to log message to discord if it's going to be delete right away
            #use logging instead.
            # if utils.contains_keywords(message.content):
            #     await message.delete()
            return

        if message.content.startswith('$delete'):
            response = await command_handler.handle(message)
        else:
            return

        await message.channel.send(response)

