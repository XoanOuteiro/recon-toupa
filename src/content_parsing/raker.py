import re
import requests
from utils.logger import Logger

class Raker:
    '''
        Manages everything related to interpreting HTML responses for attack surface and exposed data
    '''

    data = None

    logger : Logger = None

    # Regex patterns for potential API keys
    # From: https://github.com/odomojuli/regextokens
    api_key_patterns =[             
            # AWS
            r'AKIA[0-9A-Z]{16}',                     # AWS Access Key ID
            r'[0-9a-zA-Z/+]{40}',                    # AWS Secret Key
            
            # Google
            r'AIza[0-9A-Za-z-_]{35}',                # Google API Key
            r'[0-9a-zA-Z-_]{24}',                    # Google OAuth 2.0 Secret Key
            r'4/[0-9A-Za-z-_]+',                     # Google OAuth 2.0 Auth Code
            r'1/[0-9A-Za-z-]{43}|1/[0-9A-Za-z-]{64}',# Google OAuth 2.0 Refresh Token
            r'ya29\.[0-9A-Za-z-_]+',                 # Google OAuth 2.0 Access Token
            
            # GitHub
            r'ghp_[a-zA-Z0-9]{36}',                  # GitHub Personal Access Token (Classic)
            r'github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}', # GitHub Personal Access Token (Fine-Grained)
            r'gho_[a-zA-Z0-9]{36}',                  # GitHub OAuth 2.0 Access Token
            r'ghu_[a-zA-Z0-9]{36}',                  # GitHub User-to-Server Access Token
            r'ghs_[a-zA-Z0-9]{36}',                  # GitHub Server-to-Server Access Token
            r'ghr_[a-zA-Z0-9]{36}',                  # GitHub Refresh Token
            
            # Stripe
            r'sk_live_[0-9a-zA-Z]{24}',              # Stripe Secret Key
            
            # Slack
            r'xox[baprs]-[0-9a-zA-Z]{10,48}',        # Slack Token
            
            # Foursquare
            r'R_[0-9a-f]{32}',                       # Foursquare Secret Key
            
            # Picatic
            r'sk_live_[0-9a-z]{32}',                 # Picatic API Key
            
            # Square
            r'sqOatp-[0-9A-Za-z-_]{22}',             # Square Access Token
            r'q0csp-[0-9A-Za-z-_]{43}',              # Square OAuth Secret
            
            # PayPal / Braintree
            r'access_token\$production\$[0-9a-z]{161}[0-9a]{32}', # PayPal / Braintree Access Token
            
            # Twilio
            r'55[0-9a-fA-F]{32}',                    # Twilio Access Token
            
            # Mailgun
            r'key-[0-9a-zA-Z]{32}',                  # Mailgun Access Token
            
            # MailChimp
            r'[0-9a-f]{32}-us[0-9]{1,2}',            # MailChimp Access Token
            
            # Heroku
            r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', # Heroku API Key
            
            # Facebook
            r'EAACEdEose0cBA[0-9A-Za-z]+',           # Facebook Access Token
            
            # Instagram
            r'[0-9a-fA-F]{7}\.[0-9a-fA-F]{32}',      # Instagram OAuth 2.0 Token
            r'(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)', # Instagram Username
            r'(?:#)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:.(?!.))){0,28}(?:[A-Za-z0-9_]))?)', # Instagram Hashtag
            
            # Twitter
            r'[1-9][0-9]+-[0-9a-zA-Z]{40}',           # Twitter Access Token
            r'(^|[^@\w])@(\w{1,15})\b',              # Twitter Username
            
            # Base64
            r'^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$', # Base64 Format
            
            # Amazon Marketing Services
            r'amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-10-9a-f1{4}-[0-9a]{4}-[0-9a-f]{12}', # Auth Token
        ]

    def __init__(self):
        '''
            Instances an object of this class.
            Content to parse is passed to process()
        '''
        self.logger = Logger()


    def process(self, url:str):
        '''
            Analyzes the data and calls for printing of any
            potentially valuable info found
        '''

        self.data = self.requestInfo(url)
        if self.data:
            self.logger.log_api_rake_start(url)

            results = self.getApiKeys()
            self.logger.log_api_results(results)
            
        else:
            self.logger.log_unreachable(url)

    def getApiKeys(self):
        '''
            Parses data with regex to attempt to extract 
            API keys
        '''        
        api_results = []
        
        for pattern in self.api_key_patterns:
            found_keys = re.findall(pattern, self.data)
            api_results.extend(found_keys)
        
        return api_results

    def requestInfo(self, url : str):
        '''
            Attempt to get HTML response for input url
            Returns HTMl as str if found, returns None otherwise
        '''

        try:
            response = requests.get(url)

            if response.status_code == 200:
                    return response.text
            else:
                return None
            
        except Exception as error:
            return None
        


