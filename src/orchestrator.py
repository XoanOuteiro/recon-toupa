from src.directory_enumeration.directory_bruteforcer import DirectoryBruteforcer

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
        bruteforcer_module = DirectoryBruteforcer(self.args.bruteforceDirectory)
        bruteforcer_module.run()

    
    def run(self):
        '''
            Parses the stored arguments and executes the corresponding modules
        '''

        if self.args.bruteforceDirectory:

            self.run_module_bruteDir()

        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')
