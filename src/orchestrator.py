from directory_enumeration.directory_bruteforcer import DirectoryBruteforcer

class Orchestrator:
    '''
        Controller of module loading 
    '''

    def __init__(self, args):
        '''
            Instances an Orchestrator to manage the launch of the required module passed in args
        '''

        self.args = args

    def run(self):
        '''
            Parses the stored arguments and executes the corresponding modules
        '''

        if self.args.bruteforceDirectory and self.args.url:

            run_module_bruteDir(self)

        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')


    def run_module_bruteDir(self):
            bruteforcer_module = DirectoryBruteforcer(self.arg.url, self.args.bruteforceDirectory)
            bruteforcer_module.run()