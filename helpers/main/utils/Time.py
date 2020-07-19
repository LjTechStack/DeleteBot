class Time:

    def __init__(self):
        self.day = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.error = None

    def log_time(self, character, string_time_value):
        try:
            value = int(string_time_value)
        except ValueError:
            self.error = 'time mismatch'
            return

        if character == 'd':
            if value < 0 or value > 14:
                self.error = 'Error parsing time, day can only be between 0-14'
                return
            self.day = value
        elif character == 'h':
            if value < 0 or value > 24:
                self.error = 'Error parsing time, correct format for hours is 0-24'
                return
            self.hours = value
        elif character == 'm':
            if value < 0 or value > 60:
                self.error = 'Error parsing time, correct format for minutes is 0-60'
                return
            self.minutes = value
        elif character == 's':
            if value < 0 or value > 60:
                self.error = 'Error parsing time, correct format for seconds is 0-60'
                return
            self.seconds = value
        else:
            self.error = 'Error parsing time, correct format for time is xdyhzm, where xyz are integer values'
