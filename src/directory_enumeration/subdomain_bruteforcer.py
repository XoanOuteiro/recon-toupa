'''
    >> RECON-TOUPA SubdomainBruteforcer Module
    >> Developed by: @XoanOuteiro
'''

import requests
from utils.logger import Logger

class SubdomainBruteforcer:
    def __init__(self, target: str, wordlistPath: str = 'wordlists/subdomain_enum/shubs-subdomains.txt'):
        self.target = target
        self.wordlistPath = wordlistPath
        self.logger = Logger()
        self.discovered_directories = set()

    def check_subdomain(self, subdomain):
        '''
            Checks if a subdomain exists on the target server and logs the discovery
        '''
        url = f"http://{subdomain}.{self.target}"
        
        try:
            response = requests.get(url)
            if response.status_code in [200, 300, 301, 302]:
                self.logger.log_subdomain_bruteforceDiscovery(url, response.status_code)

        except requests.RequestException as e:
            print(f'Error checking {url}: {e}')

    def run(self):
        '''
            Runs the subdomain brute force attack using the wordlist
        '''
        try:
            with open(self.wordlistPath, 'r') as file:
                for line in file:
                    subdomain = line.strip()
                    if subdomain not in self.discovered_directories:
                        self.discovered_directories.add(subdomain)
                        self.check_subdomain(subdomain)

        except FileNotFoundError:
            print(f"Wordlist file not found: {self.wordlistPath}")
