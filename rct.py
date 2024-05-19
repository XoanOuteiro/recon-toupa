'''
    >> RECON-TOUPA Launcher
    >> Developed by: @XoanOuteiro

    This script is used to control the launch of all Recon-Toupa modules
'''

import argparse
from utils.header import HeaderPrinter as logo


def buildArgs():
    '''
        Builds an argsparse object and populates it with all the modules flags
    '''

    parser = argparse.ArgumentParser(description="Recon-Toupa")

    # version flag
    parser.add_argument('-v', '--version', action='version', version=f'{logo.header}')

    # DIRECTORY DISCOVERY module flags
    parser.add_argument('-bD', '--bruteforceDirectory', help='Toggle directory discovery via bruteforce enumeration. [Requires: --url]')
    parser.add_argument('-cD', '--crawlDirectory', help='Toggle directory discovery by crawling the DOM of any link found in the target URL. [Requires: --url]')
    
    # SUBDOMAIN DISCOVERY module flags
    parser.add_argument('-bS', '--bruteforceSubdomain', help='Toggle subdomain discovery via bruteforce enumeration. [Requires: --url]')
    parser.add_argument('-oS', '--osintSubdomain', help='Toggle subdomain enumeration via consulting open source intelligence. [Requires: --url]')

    # INJECTION POINT module flags
    parser.add_argument('-fS', '--findSurface', help='Toggle automatic discovery of potential injection points within a URLs DOM. [Requires: --url]')
    parser.add_argument('-r', '--rake', help='Toggle the recovery of potential sensitive info in the specified URLs DOM (eg. APIKeys and other hardcoded values) [Requires: --url]')

    #---

    # SETTINGS FLAGS
    # !!! - Currently all enumerations run at 1 thread and 2 requests/second. 14/May/2024
    parser.add_argument('-u', '--url', help='The specified target of any module called before this flag.')


    #--- END ---
    return parser.parse_args()

def startProgram(args):
    '''
        Prints logo, header and instances an Orchestrator entity
    '''

    print(logo.logoAscii)
    print(logo.header)

    mainOrchestrator = Orchestrator(args)
    mainOrchestrator.run()


if __name__ == '__main__':

    startProgram(buildArgs())