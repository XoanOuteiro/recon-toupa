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
    extracted_urls = []

    def __init__(self):
        self.logger = Logger()  # Fix the logger initialization

    def target(self, url):
        '''
            Attempts to check the DOM content
            of a HTTP request against many wordlists
            for common injection points
        '''

        content = self.getTarget(url)

        if content:

            self.logger.log_surface_finder_start(url)
            self.parseForAllParams(content)
            self.parseForOR()
            # self.parseForXSS(content)
            for url in self.extracted_urls:
                self.logger.log_url_with_params(url)  # Log each URL with parameters

        else:
            self.logger.log_unreachable(url)

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
                    # Create a regex pattern to match the current word
                    or_pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)

                    # Check each extracted URL for matches against the current word pattern
                    for url in self.extracted_urls:

                        if or_pattern.search(url):
                            self.logger.log_potential_open_redirect(url, word)

