from datetime import datetime
from colorama import init, Fore, Style

class Logger:
    '''
        A simple logger class to abstract logging and printing mechanisms
    '''

    def __init__(self):
        init(autoreset=True)

    def log_bruteforceDiscovery(self, message, status_code):
        '''
            Log a message and add a datetime timestamp with colored output based on status_code
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        color = None

        if 200 <= status_code < 300:
            color = Fore.GREEN
        elif 300 <= status_code < 400:
            color = Fore.YELLOW
        elif 400 <= status_code < 500:
            color = Fore.RED
        elif 500 <= status_code < 600:
            color = Fore.BLUE

        if color:
            print(f'[{current_time}] - {color}{message}{Style.RESET_ALL}')  # Reset color after message
        else:
            print(f'[{current_time}] - {message}')