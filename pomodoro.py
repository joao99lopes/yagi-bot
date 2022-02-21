import time

DEFAULT_WORK_TIME = 25
DEFAULT_REST_TIME = 5
DEFAULT_NUMBER_OF_ROUNDS = 4
ERROR_ONGOING = "ERROR: There's a Pomodoro session ongoing.\nPlease stop it in order to change its settings."
HELP = "`!pomodoro start`\n`!pomodoro work-time <number of minutes>`\n`!pomodoro rest-time <number of minutes>`\n`!pomodoro round-limit <number of rounds>`\n`!pomodoro help`"

class Pomodoro:
    def __init__(self):
        self.is_running = False
        self.work_time = DEFAULT_WORK_TIME
        self.rest_time = DEFAULT_REST_TIME
        self.nr_rounds = DEFAULT_NUMBER_OF_ROUNDS
    

    def set_is_running(self, is_running):
        self.is_running = is_running

    def get_is_running(self):
        return self.is_running


    def set_work_time(self, work_time):
        if not self.is_running:
            self.work_time = work_time
        else:
            return ERROR_ONGOING
            
    def get_work_time(self):
        return int(self.work_time)
            

    def set_rest_time(self, rest_time):
        if not self.is_running:
            self.rest_time = rest_time
        else:
            return ERROR_ONGOING

    def get_rest_time(self):
        return int(self.rest_time)
        

    def set_number_of_rounds(self, nr_rounds):
        if not self.is_running:
            self.nr_rounds = nr_rounds
        else:
            return ERROR_ONGOING

    def get_number_of_rounds(self):
        return int(self.nr_rounds)



#    def start(self):
    
    def get_help(self):
        return HELP


                