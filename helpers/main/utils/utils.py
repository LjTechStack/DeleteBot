import logging
import helpers.main.utils.messages as messages
from helpers.main.utils.Time import Time

logging.basicConfig(level=logging.INFO,
                    format='%(name)s - %(levelname)s: %(message)s')
logger = logging.getLogger('utils')


DELETE_MESSAGE = {messages.DELETE}


def contains_keywords(string):
    results = next((substring for substring in DELETE_MESSAGE if substring in string), None)

    if results:
        logger.debug('Matched: ' + results)
        return True
    else:
        logger.debug('Nothing Matched')
        return False


def get_day_hour_min(string_time):
    temp_time = ''
    time = Time()
    for character in string_time:
        if character.isnumeric() or character == '-':
            temp_time += character
        else:
            time.log_time(character, temp_time)
            temp_time = ''
            if time.error:
                break
    return time


def get_min(string_time):
    temp_time = ''
    time = Time()
    for character in string_time:
        if character.isnumeric() or character == '-':
            temp_time += character
        elif character == 'm':
            time.log_time(character, temp_time)
            temp_time = ''
            if time.error:
                break
        else:
            temp_time = ''
    return time

