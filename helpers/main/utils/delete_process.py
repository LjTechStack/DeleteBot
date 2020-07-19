import logging
from datetime import datetime, timedelta
import helpers.main.utils.utils as utils
import asyncio

logging.basicConfig(level=logging.INFO,
                    format='%(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger('delete_process')

is_delete_scheduler_running = False

async def do_user_delete(command, message):
    string_time = command[-1:].pop()
    users = message.mentions
    time = utils.get_day_hour_min(string_time)
    if time.error:
        return time.error

    logger.info("get the last param from messages: " + string_time)
    if len(users) == 1 and message.author in users:
        return await start_delete_process(message, time, users)
    elif message.author.guild_permissions.manage_messages:
        return await start_delete_process(message, time, users)
    else:
        return message.author.name + ' does not have permission to delete other users messages'


async def start_delete_process(messages, time, users=None):
    logger.info("starting delete process")
    count = 0

    past_date = datetime.utcnow() - timedelta(hours=time.hours, days=time.day, minutes=time.minutes, seconds=time.seconds)

    async for message in messages.channel.history(limit=10000):
        if past_date > message.created_at:
            break
        if not users:
            logger.info(message)
            await message.delete()
            count += 1
        elif message.author in users:
            logger.info(message)
            await message.delete()
            count += 1

    return count


def check_if_scheduler_is_running():
    return is_delete_scheduler_running


async def start_delete_timer(string_time, message):
    timer = utils.get_day_hour_min(string_time)
    global is_delete_scheduler_running

    if (timer.minutes > 0 or timer.seconds > 0) and not is_delete_scheduler_running:
        is_delete_scheduler_running = True
        while is_delete_scheduler_running:
            await asyncio.sleep(timer.minutes*60+timer.seconds-1)
            if is_delete_scheduler_running:
                await start_delete_process(message, timer)
    else:
        return False


def stop_delete_timer():
    global is_delete_scheduler_running
    if is_delete_scheduler_running:
        is_delete_scheduler_running = False
        return True
    return False
