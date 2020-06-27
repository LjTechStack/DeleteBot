import discord
from datetime import datetime, timedelta
from help_menu.help import help
from helpers.main.utils import utils, keys
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        if utils.containsKeywords(message.content):
            message.delete()
        return

    action = "something to start with"

    if message.content.startswith('$delete'):
        command = message.content.split(" ")
        if len(command) < 3:
            number_of_messages = await do_command(command[1:], message)
            action = "we have deleted: " + str(number_of_messages) + " messages"
        elif command[1] == 'help':
            help()
            action = "helping"

        else:
            action = "To use $delete help"

        await message.channel.send(action)


async def do_command(command, message):
    if command[0].replace('!','') == message.author.mention.replace('!',''):
        return await start_delete_process(message)


async def start_delete_process(message):
    count = 0
    yesterday = datetime.now() - timedelta(hours=12)

    async for elem in message.channel.history(limit=10000):
        if yesterday < elem.created_at:
            break
        if elem.author == message.author:
            print(elem)
            await elem.delete()
            count += 1
    return count


client.run(keys.CLIENT_KEY)
