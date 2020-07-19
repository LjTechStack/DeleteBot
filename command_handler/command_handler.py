import logging
import helpers.main.utils.delete_process as delete

from help_menu import help

logger = logging.getLogger('command.handler')


async def handle(message):
    # used to split the message by spaces ignoring any extra spaces
    command = ' '.join(message.content.split()).split(' ')
    if len(command) < 3:
        if len(command) == 2 and command[1] == 'help':
            action = help.print_help()
        else:
            action = 'To get a list of commands use: $delete help'
    else:
        if command[1] != 'timer':
            messages = await delete.do_user_delete(command[1:], message)
            # if messages was an error message, display that, else message equivalent to number of messages deleted
            if isinstance(messages, str):
                action = messages
            else:
                action = 'we have deleted: ' + str(messages) + ' messages'
        else:
            if command[-1] == 'stop':
                logger.info('stopping scheduler')
                was_stoped = delete.stop_delete_timer()
                if was_stoped:
                    action = 'Delete scheduler has been stopped'
                else:
                    action = 'Scheduler was not running'

            else:
                logger.info('starting scheduler')
                if not delete.is_delete_scheduler_running:
                    action = 'Delete scheduler has been started'
                else:
                    action = "Delete scheduler has already been started"
                await delete.start_delete_timer(command[-1], message)

    return action
