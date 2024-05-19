from datetime import datetime

class Logger:
    '''
        A simple logger class to abstract logging and printing mechanisms
    '''

    def log(self, message):
        '''
            Log a message and add a datetime timestamp
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'[{current_time}] - {message}')