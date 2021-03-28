#Code begins
#!/usr/bin/python3
import requests
import argparse
from colorama import Fore

def subdomainer(domain):
	file = open("subdomains.txt")
	content = file.read()
	subdomains = content.splitlines()
	for subdomain in subdomains:
		url = f"http://{subdomain}.{domain}"
		try:
			requests.get(url)
		except requests.ConnectionError:
			pass
		else:
			print(Fore.BLUE + "[+] Discovered subdomain:", url)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--domain',help='Target domain ')
	args = parser.parse_args()
	print(Fore.RED + '''

  █████▒▄▄▄       ██ ▄█▀▓█████  ██▓▄▄▄█████▓
▓██   ▒▒████▄     ██▄█▒ ▓█   ▀ ▓██▒▓  ██▒ ▓▒
▒████ ░▒██  ▀█▄  ▓███▄░ ▒███   ▒██▒▒ ▓██░ ▒░
░▓█▒  ░░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ░██░░ ▓██▓ ░ 
░▒█░    ▓█   ▓██▒▒██▒ █▄░▒████▒░██░  ▒██▒ ░ 
 ▒ ░    ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░▓    ▒ ░░   
 ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░ ▒ ░    ░    
 ░ ░     ░   ▒   ░ ░░ ░    ░    ▒ ░  ░      > v1.0 Subdomain Finder
             ░  ░░  ░      ░  ░ ░           

''')

	if args.domain:
		subdomainer(args.domain)
		exit()
