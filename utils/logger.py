'''
    >> RECON-TOUPA Logger Module
    >> Developed by: @XoanOuteiro
'''

from datetime import datetime
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text

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
        pass

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

    def log_unreachable(self, url):
        '''
            Logs an error message for URLs that cannot be requested
        '''
        console.print(Panel(f'!!! -- TARGET UNREACHABLE -- @{url}', border_style='client_error'))

    def log_api_results(self, results):
        '''
            Logs the results for API key raking
        '''
        if len(results) > 0:
            for item in results:
                console.print(Panel(f'Potential key: {item}', border_style='api_key_found'))
        else:
            console.print(Panel(f'!> No API keys found at target HTML', border_style='nothing_found'))

    def log_api_rake_start(self, url):

        console.print(Panel(f'>> Scraping {url} for API keys...', border_style='start_message'))

    def log_surface_finder_start(self, url):

        console.print(Panel(f'>> Scraping {url} for attack surface...', border_style='start_message'))

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

        self.console.print(Panel(log_message, title="Potential Open Redirect", border_style="bold blue"))

    def log_url_with_params(self, url):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        time_prefix = Text("Time: ", style="bold blue")
        time_text = Text(current_time, style="white")

        url_prefix = Text("URL: ", style="bold blue")
        url_text = Text(url, style="cyan")

        type_prefix = Text("Type: ", style="bold blue")
        type_text = Text("Generic", style="white")

        log_message = time_prefix + time_text + "\n" + url_prefix + url_text + "\n" + type_prefix + type_text

        self.console.print(Panel(log_message, title="URL with Parameters", border_style="generic"))