from utils.logger import Logger
import re
import requests

class SurfaceFinder:

    logger : Logger = None

    or_wordlist_path = 'wordlists/injection_points/open_redirect.txt'  # Path for common injection points for open redirect vulnerabilities

    def __init__(self):
        logger = Logger()