import requests

class DirectoryBruteforcer:
    '''
        Used to discover attack surface via HTTP response codes to different wordlists
        appended to a URL
    '''

    def __init__(self, target : str, wordlistPath : str = '../../wordlists/directory_bruteforce/directory-list-2.3-medium.txt'):
        '''
            Instances a Directory bruteforcer for the given target and using the provided wordlist
            for enumeration
        '''

        self.target = target
        self.wordlistPath = wordlistPath