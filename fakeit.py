#code for subdomain finder
#proxies for subdomain finder
#email the subdomains.

pip3 install requests
import requests

domain = "apple.com"
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
        print("[+] Discovered subdomain:", url)