'''
    >> RECON-TOUPA Orchestrator Script
    >> Developed by: @XoanOuteiro
'''

from src.directory_enumeration.directory_bruteforcer import DirectoryBruteforcer
from src.directory_enumeration.subdomain_bruteforcer import SubdomainBruteforcer
from src.content_parsing.raker import Raker
from src.content_parsing.surface_finder import SurfaceFinder

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

        calculated_timeout = int(self.args.pause) if self.args.pause is not None else 0

        bruteforcer_module = DirectoryBruteforcer(self.args.url, crawl= self.args.crawl, rake = self.args.rake, surfacer=self.args.findSurface, ruled_timeout=calculated_timeout)
        bruteforcer_module.run()

    def run_module_rake(self):
        raker = Raker().process(self.args.url)

    def run_surface_finder(self):
        surface_Finder = SurfaceFinder()
        surface_Finder.target(self.args.url)

    def run_subdomain_bruteforcer(self):
        sbd = SubdomainBruteforcer(self.args.url)
        sbd.run()

    
    def run(self):
        '''
            Parses the stored arguments and executes the corresponding modules
        '''

        if self.args.bruteforceDirectories and self.args.url:

            self.run_module_bruteDir()

        if self.args.rake and self.args.url:

            self.run_module_rake()

        if self.args.findSurface and self.args.url:

            self.run_surface_finder()

        if self.args.bruteforceSubdomains and self.args.url:
            
            self.run_subdomain_bruteforcer()

        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')
