'''
    >> RECON-TOUPA SurfaceFinder Module
    >> Developed by: @XoanOuteiro
'''

from utils.logger import Logger
from bs4 import BeautifulSoup
import re
import requests

class SurfaceFinder:

    logger: Logger = None

    or_wordlist_path = 'wordlists/injection_points/open_redirect.txt'  # Path for common injection points for open redirect vulnerabilities
    sqli_wordlist_path = 'wordlists/injection_points/sqli.txt'  # Path for common injection points for sqli vulnerabilities
    xss_wordlist_path = 'wordlists/injection_points/xss.txt'  # Path for common injection points for xss vulnerabilities
    extracted_urls = []

    def __init__(self):
        self.logger = Logger()  # Fix the logger initialization

    def target(self, url, content = None):
        '''
            Attempts to check the DOM content
            of a HTTP request against many wordlists
            for common injection points
        '''

        if content is None:
            content = self.getTarget(url)

            if content:
                self.parseContent(url, content)
            else:
                self.logger.log_unreachable(url)

        else:
            self.parseContent(url, content)

    def parseContent(self, url, content):
            self.logger.log_surface_finder_start(url)
            self.parseForAllParams(content)
            self.parseForOR()
            self.parseForXSS()
            self.parseForSQLI()
            for url in self.extracted_urls:
                self.logger.log_url_with_params(url)  # Log each URL with parameters

    def getTarget(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as error:
            self.logger.log_error(f"Error fetching {url}: {error}")
            return None

    def parseForAllParams(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        urls = []

        # Find all tags and check all attributes for URLs with parameters
        for tag in soup.find_all(True):  # Find all tags
            for attr, value in tag.attrs.items():
                if isinstance(value, str) and '?' in value:
                    urls.append(value)

        self.extracted_urls = urls

    def parseForOR(self):
        with open(self.or_wordlist_path, 'r') as file:
            
            for line in file:
                word = line.strip()

                if word:
                    # Check each extracted URL for the presence of the current word as a substring
                    for url in self.extracted_urls:
                        if word.lower() in url.lower():  # Case insensitive check
                            self.logger.log_potential_open_redirect(url, word)

    def parseForXSS(self):
        with open(self.xss_wordlist_path, 'r') as file:

            for line in file:
                word = line.strip()

                if word:
                    for url in self.extracted_urls:
                        if word.lower() in url.lower():
                            self.logger.log_potential_xss(url, word)

    def parseForSQLI(self):
        with open(self.sqli_wordlist_path, 'r') as file:

            for line in file:
                word = line.strip()

                if word:
                    for url in self.extracted_urls:
                        if word.lower() in url.lower():
                            self.logger.log_potential_sqli(url, word)
        

