class Orchestrator:
    '''
        Controller of module loading 
    '''

    def __init__(self, args):
        '''
            Instances an Orchestrator to manage the launch of the required module passed in args
        '''

        self.args = args

    def run():

        if args.bruteforceDirectory and args.url:

            pass # TODO

        else:
            print('[!!!] Usage incorrect, please check -h/--help for instructions.')
