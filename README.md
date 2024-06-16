# Recon-Toupa

![Resetti Logo](./images/resetti_logo.png)

All-in-one reconnaissance tool made to simplify reconnaissance in Bug Bounties and other Web Pentests.

## THIS IS A WIP!!!

This application is currently a WIP (work-in-progress), usage of any script on a live target without full knowledge of its actions is strongly disadvised as it may have ethical and/or legal implications.

## What can this tool do?

- Content-Discovery: Bruteforce Fuzzing
- Content-Discovery: Directory Crawling
- Content-Discovery: Bruteforce subdomain enumeration
- Content-Discovery: OSINT subdomain enumeration
- Injection-Point Discovery: Open Redirect, XSS, SQLi ...
- Data-Parsing: Automated API key discovery
- Report-Creation: Per target reports

## Installation

Currently there are no installation methods, but the install.sh mentioned below will soon be available as the app reaches 0.2

### Debian based OS

First clone the repository and move into it's folder:
``` shell
git clone https://github.com/XoanOuteiro/recon-toupa
cd recon-toupa
```
Then install the requirements with Python 3.12
``` shell
pip install -r requirements.txt
```

### Arch based OS
First clone the repository and move into it's folder:
``` shell
git clone https://github.com/XoanOuteiro/recon-toupa
cd recon-toupa
```
Then use the install.sh script to use pacman to install the required packages for Python 3.12:
``` shell
sh ./install.sh
```

## Usage

| Command | Description |
| --- | --- |
| -h / --help | Displays a brief description of the usage of the app |
| -v / --version | Displays the current build version |
| -u / --url | Needed for every attack module. Specifies the URL to be attacked, needs a protocol) |
| -bD / --bruteforceDirectories | Specifies to load de directory bruteforcer module. Uses a SecList wordlist |
| -c / --crawl | Needs bruteforcer to be enabled. Specifies to scrape HTML response of any valid bruteforce entry for URLs |
| -r / --rake | Parses HTML data, checking against a list of RegEx ressembling common API keys, can be used along -bD and -c or individually |
| -fS / --findSurface | Parses HTML data against an ammount of wordlists to extract all parameters and highlight potentially vulnerable ones |


