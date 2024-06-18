'''
    >> RECON-TOUPA Orchestrator Script
    >> Developed by: @XoanOuteiro
'''

from src.directory_enumeration.directory_bruteforcer import DirectoryBruteforcer
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
        bruteforcer_module = DirectoryBruteforcer(self.args.url, crawl= self.args.crawl, rake = self.args.rake, surfacer=self.args.findSurface)
        bruteforcer_module.run()

    def run_module_rake(self):
        raker = Raker().process(self.args.url)

    def run_surface_finder(self):
        surface_Finder = SurfaceFinder()
        surface_Finder.target(self.args.url)

    
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

        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')
