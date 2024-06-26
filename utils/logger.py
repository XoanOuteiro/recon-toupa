'''
    >> RECON-TOUPA Logger Module
    >> Developed by: @XoanOuteiro
'''

from datetime import datetime
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
import os

theme = Theme({
    "success": "green",
    "redirect": "yellow",
    "nothing_found": "yellow",
    "client_error": "red",
    "server_error": "blue",
    "child_content": "magenta",
    "api_key_found": "blue",
    "start_message": "green"
})

console = Console(theme=theme)

class Logger:
    '''
        A simple logger class to abstract logging and printing mechanisms
    '''

    def __init__(self):
        log_dir = './info'
        log_file = 'recon.log'
        self.log_path = os.path.join(log_dir, log_file)

        # Ensure the directory exists
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Ensure the file exists
        if not os.path.exists(self.log_path):
            with open(self.log_path, 'w') as f:
                pass

    def _write_to_log(self, message):
        '''
            Write a message to the log file with a datetime timestamp
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_path, 'a') as log_file:
            log_file.write(f'[{current_time}] {message}\n')

    def log_bruteforceDiscovery(self, message, status_code):
        '''
            Log a message and add a datetime timestamp with colored output based on status_code
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        prefix_color = "bold blue"

        if 200 <= status_code < 300:
            color = "success"
        elif 300 <= status_code < 400:
            color = "redirect"
        elif 400 <= status_code < 500:
            color = "client_error"
        elif 500 <= status_code < 600:
            color = "server_error"
        else:
            color = None

        dt_prefix = Text("DT: ", style=prefix_color)
        dt_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style=prefix_color)
        url_text = Text(message, style="cyan")

        rc_prefix = Text("RC: ", style=prefix_color)
        rc_text = Text(str(status_code), style=color)

        log_message = dt_prefix + dt_text + "\n" + url_prefix + url_text + "\n" + rc_prefix + rc_text
        
        if color:
            console.print(Panel(log_message, border_style=color))
        else:
            console.print(Panel(log_message))

        self._write_to_log(f'{message} discovered via bruteforce attack')

    def log_childrenContent(self, message):
        '''
            Log a message for content found by crawling with a datetime timestamp
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        prefix_color = "bold blue"

        dt_prefix = Text("DT: ", style=prefix_color)
        dt_text = Text(current_time, style="white")

        url_prefix = Text("New Directory: ", style=prefix_color)
        url_text = Text(message, style="child_content")

        log_message = dt_prefix + dt_text + "\n" + url_prefix + url_text
        
        console.print(Panel(log_message, border_style="child_content"))

        self._write_to_log(f'{message} discovered via crawler')

    def log_unreachable(self, url):
        '''
            Logs an error message for URLs that cannot be requested
        '''
        console.print(Panel(f'!!! -- TARGET UNREACHABLE -- @{url}', border_style='client_error'))
        self._write_to_log(f'tried to reach {url} but couldnt')

    def log_api_results(self, results):
        '''
            Logs the results for API key raking
        '''
        if len(results) > 0:
            for item in results:
                console.print(Panel(f'Potential key: {item}', border_style='api_key_found'))
                self._write_to_log(f'POTENTIAL KEY << {item} >> discovered via raker')
        else:
            console.print(Panel(f'!> No API keys found at target HTML', border_style='nothing_found'))

    def log_bruteforce_directory_start(self, url, timeout):

        console.print(Panel(f'>> Starting bruteforce enumeration attack against {url} with a per-req pause of {timeout} ms', border_style='start_message'))
        self._write_to_log(f'started bruteforce attack against {url}')

    def log_api_rake_start(self, url):

        console.print(Panel(f'>> Scraping {url} for API keys...', border_style='start_message'))
        self._write_to_log(f'started raker module against {url}')

    def log_surface_finder_start(self, url):

        console.print(Panel(f'>> Scraping {url} for attack surface...', border_style='start_message'))
        self._write_to_log(f'started surfaceFinder module against {url}')

    def log_potential_open_redirect(self, url, word):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_prefix = Text("Time: ", style="bold blue")
        time_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style="bold blue")
        url_text = Text(url, style="cyan")

        type_prefix = Text("Type: ", style="bold blue")
        type_text = Text("Open Redir.", style="white")

        regmatch_prefix = Text("RegMatch: ", style="bold blue")
        regmatch_text = Text(word, style="white")

        log_message = time_prefix + time_text + "\n" + url_prefix + url_text + "\n" + type_prefix + type_text + "\n" + regmatch_prefix + regmatch_text

        console.print(Panel(log_message, title="Potential Open Redirect", border_style="child_content"))

        self._write_to_log(f'found potential OR (Open Redirect) vulnerability on {url} while matching {word}')

    def log_potential_xss(self, url, word):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_prefix = Text("Time: ", style="bold blue")
        time_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style="bold blue")
        url_text = Text(url, style="cyan")

        type_prefix = Text("Type: ", style="bold blue")
        type_text = Text("XSS", style="white")

        regmatch_prefix = Text("RegMatch: ", style="bold blue")
        regmatch_text = Text(word, style="white")

        log_message = time_prefix + time_text + "\n" + url_prefix + url_text + "\n" + type_prefix + type_text + "\n" + regmatch_prefix + regmatch_text

        console.print(Panel(log_message, title="Potential XSS", border_style="child_content"))

        self._write_to_log(f'found potential XSS (Cross-Site Scripting) vulnerability on {url} while matching {word}')

    def log_potential_sqli(self, url, word):

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_prefix = Text("Time: ", style="bold blue")
        time_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style="bold blue")
        url_text = Text(url, style="cyan")

        type_prefix = Text("Type: ", style="bold blue")
        type_text = Text("SQLi", style="white")

        regmatch_prefix = Text("RegMatch: ", style="bold blue")
        regmatch_text = Text(word, style="white")

        log_message = time_prefix + time_text + "\n" + url_prefix + url_text + "\n" + type_prefix + type_text + "\n" + regmatch_prefix + regmatch_text

        console.print(Panel(log_message, title="Potential SQLi", border_style="child_content"))

        self._write_to_log(f'found potential SQLi (SQL Injection) vulnerability on {url} while matching {word}')

    def log_url_with_params(self, url):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_prefix = Text("Time: ", style="bold blue")
        time_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style="bold blue")
        url_text = Text(url, style="cyan")

        type_prefix = Text("Type: ", style="bold blue")
        type_text = Text("Generic", style="white")

        log_message = time_prefix + time_text + "\n" + url_prefix + url_text + "\n" + type_prefix + type_text

        console.print(Panel(log_message, title="URL with Parameters", border_style="child_content"))

        self._write_to_log(f'found potentially interesting URL on {url} (has parameters)')

    def log_subdomain_bruteforceDiscovery(self, url, status_code):
        '''
            Log a message and add a datetime timestamp with colored output based on status_code
        '''
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        prefix_color = "bold blue"

        if 200 <= status_code < 300:
            color = "success"
        elif 300 <= status_code < 400:
            color = "redirect"
        elif 400 <= status_code < 500:
            color = "client_error"
        elif 500 <= status_code < 600:
            color = "server_error"
        else:
            color = None

        dt_prefix = Text("DT: ", style=prefix_color)
        dt_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style=prefix_color)
        url_text = Text(message, style="cyan")

        rc_prefix = Text("RC: ", style=prefix_color)
        rc_text = Text(str(status_code), style=color)

        log_message = dt_prefix + dt_text + "\n" + url_prefix + url_text + "\n" + rc_prefix + rc_text
        
        if color:
            console.print(Panel(log_message, border_style=color))
        else:
            console.print(Panel(log_message))

        self._write_to_log(f'{message} discovered via bruteforce attack')

    def log_nonexistant_sub(self, url):
        console.print(Panel(f'>> {url} was not a valid subdomain', border_style='nothing_found'))
        self._write_to_log(f'{url} was not a valid subdomain')
