from src.directory_enumeration.directory_bruteforcer import DirectoryBruteforcer
from src.content_parsing.raker import Raker

class Orchestrator:
    '''
        Controller of module loading 
    '''

    def __init__(self, args):
        '''
            Instances an Orchestrator to manage the launch of the required module passed in args
        '''

        self.args = args

    
    def run_module_bruteDir(self):
        bruteforcer_module = DirectoryBruteforcer(self.args.url, crawl= self.args.crawl)
        bruteforcer_module.run()

    def run_module_rake(self):
        raker = Raker(self.args.url) # Launches process method at startup if and only if url can be reached

    
    def run(self):
        '''
            Parses the stored arguments and executes the corresponding modules
        '''

        if self.args.bruteforceDirectories and self.args.url:

            self.run_module_bruteDir()

        if self.args.rake and self.args.url:

            self.run_module_rake()


        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')
