def print_help():
    return 'menu\n' \
           '1) $delete {@yourself} {time*} - delete your own messages based on time specified \n' \
           '2) $delete {@tag} {@tagx} {time*} - delete messages from user-tag ' \
           'based on time specified if you contain the permission: manage_messages\n' \
           '3) $delete timer {time*} - delete messages using an interval scheduler as specified, ' \
           'you must contain the permission: manage_messages \n' \
           '4) $delete timer stop - stop the delete scheduler \n' \
           '*time structure: xdyhzm where x = |0-14|, y = |0-24| z=|0-60| ex. 1d2h30m'

