import requests
from utils.logger import Logger

class DirectoryBruteforcer:
    '''
        Used to discover attack surface via HTTP response codes to different wordlists
        appended to a URL
    '''

    logger : Logger = None

    def __init__(self, target : str, wordlistPath : str = '../../wordlists/directory_bruteforce/directory-list-2.3-medium.txt'):
        '''
            Instances a Directory bruteforcer for the given target and using the provided wordlist
            for enumeration
        '''
        self.logger = Logger()

        self.target = target
        self.wordlistPath = wordlistPath


    def check_directory(self, directory):
        '''
            Checks if a directory exists on the target server
        '''
        url = self.target + directory

        try:

            response = requests.get(url)
            if response.status_code in [200, 301]:
                self.logger.log(url, response.status_code)

        except requests.RequestException as e:
            print(f'Error checking {url}: {e}')


    def run(self):
        '''
            Runs the directory brute force attack using the wordlist
        '''
        try:

            with open(self.wordlistPath, 'r') as file:

                for line in file:

                    directory = line.strip()
                    self.check_directory(directory)

        except FileNotFoundError:
            print(f"Wordlist file not found: {self.wordlistPath}")