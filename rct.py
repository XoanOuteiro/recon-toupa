'''
    >> RECON-TOUPA Launcher
    >> Developed by: @XoanOuteiro

    This script is used to control the launch of all Recon-Toupa modules
'''

import argparse
from utils.header import HeaderPrinter
from src.orchestrator import Orchestrator


def buildArgs():
    '''
        Builds an argsparse object and populates it with all the modules flags
    '''

    parser = argparse.ArgumentParser(description="Recon-Toupa")

    # version flag
    parser.add_argument('-v', '--version', action='version', version=f'{HeaderPrinter.currentVersion}')

    # DIRECTORY DISCOVERY module flags
    parser.add_argument('-bD', '--bruteforceDirectories', help='Toggle directory discovery via bruteforce enumeration.')
    parser.add_argument('-c', '--crawl', action='store_true', help='Toggle directory discovery by crawling the DOM of any link found in the target URL. [Required -bD]')
    
    # SUBDOMAIN DISCOVERY module flags
    parser.add_argument('-bS', '--bruteforceSubdomains', help='Toggle subdomain discovery via bruteforce enumeration.')
    parser.add_argument('-oS', '--osintSubdomain', help='Toggle subdomain enumeration via consulting open source intelligence.')

    # INJECTION POINT module flags
    parser.add_argument('-fS', '--find_Surface', help='Toggle automatic discovery of potential injection points within a URLs DOM.')
    parser.add_argument('-r', '--rake', help='Toggle the recovery of potential sensitive info in the specified URLs DOM (eg. APIKeys and other hardcoded values)')

    #---

    # SETTINGS FLAGS
    # !!! - Currently all enumerations run at 1 thread and 2 requests/second. 14/May/2024W


    #--- END ---
    return parser.parse_args()

def startProgram(args):
    '''
        Prints logo, header and instances an Orchestrator entity
    '''

    header = HeaderPrinter()
    header.print_header_and_logo()

    mainOrchestrator = Orchestrator(args)
    mainOrchestrator.run()


if __name__ == '__main__':

    startProgram(buildArgs())