import datetime

class TimeOfDay:

    @staticmethod
    def get_current_hour():
        return datetime.datetime.now().hour

    @staticmethod
    def get_time_of_day(current_hour):
        if 5 <= current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 18:
            return "afternoon"
        elif 18 <= current_hour < 22:
            return "evening"
        else:
            return "night"