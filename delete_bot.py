import discord
from datetime import datetime, timedelta

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$delete'):
        command = message.content.split(" ")
        if len(command) == 3:
            number_of_messages = await do_command(command[1:], message)
            action = "we have deleted: " + str(number_of_messages) + " messages"
        else:
            action = "we could not process your request."

        await message.channel.send(action)


async def do_command(command, message):
    if command[0].replace('!','') == message.author.mention.replace('!',''):
        return await start_delete_process(message)



async def start_delete_process(message):
    count = 0
    yesterday = datetime.now() - timedelta(hours=12)

    async for elem in message.channel.history(limit=1000):
        if elem.author == message.author:
            if yesterday < elem.created_at:
                print(elem)
                await elem.delete()
                count += 1

            else:
                break
    return count


client.run('bot client_id')
