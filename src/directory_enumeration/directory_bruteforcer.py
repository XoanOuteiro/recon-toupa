'''
    >> RECON-TOUPA DirectoryBruteforcer Module
    >> Developed by: @XoanOuteiro
'''

import requests
import re
from utils.logger import Logger
from src.content_parsing.raker import Raker

class DirectoryBruteforcer:
    '''
        Used to discover attack surface via HTTP response codes to different wordlists
        appended to a URL
    '''

    raker : Raker = None
    logger: Logger = None

    def __init__(self, target: str, wordlistPath: str = 'wordlists/directory_bruteforce/directory-list-2.3-medium.txt', crawl: bool = False, rake: bool = False):
        '''
            Instances a Directory bruteforcer for the given target and using the provided wordlist
            for enumeration. If crawl is True, it will parse HTML content to find additional directories.
        '''

        if rake:
            self.raker = Raker()

        print('>> Bruteforcing directories ...')

        self.logger = Logger()

        self.target = target.rstrip('/')
        self.wordlistPath = wordlistPath
        self.crawl = crawl
        self.rake = rake
        self.discovered_directories = set()

    def check_directory(self, directory):
        '''
            Checks if a directory exists on the target server and parses HTML to find more directories if crawl is enabled
        '''
        url = self.target + '/' + directory

        try:
            response = requests.get(url)
            if response.status_code in [200, 300, 301, 302]:
                self.logger.log_bruteforceDiscovery(url, response.status_code)
                if self.crawl:
                    self.parse_html_for_links(response.text)
                if self.rake:
                    results = self.raker.getApiKeys(response.text)
                    self.logger.log_api_results(results)

        except requests.RequestException as e:
            print(f'Error checking {url}: {e}')

    def parse_html_for_links(self, html):
        '''
            Parses HTML to find local URLs and adds them to the list of directories to check
        '''
        local_urls = re.findall(r'href=[\'"]?([^\'" >]+)', html)
        for url in local_urls:
            if url.startswith('/'):
                url = url.lstrip('/')
            if not url.startswith('http') and url not in self.discovered_directories:
                self.discovered_directories.add(url)
                self.logger.log_childrenContent(url)

    def run(self):
        '''
            Runs the directory brute force attack using the wordlist
        '''
        try:
            with open(self.wordlistPath, 'r') as file:
                for line in file:
                    directory = line.strip()
                    if directory not in self.discovered_directories:
                        self.discovered_directories.add(directory)
                        self.check_directory(directory)

            if self.crawl:
                # Check newly discovered directories
                additional_dirs = list(self.discovered_directories)
                while additional_dirs:
                    directory = additional_dirs.pop(0)
                    self.check_directory(directory)
                    additional_dirs = list(set(self.discovered_directories) - set(additional_dirs))

        except FileNotFoundError:
            print(f"Wordlist file not found: {self.wordlistPath}")
