from urllib.parse import urlunparse, urlparse
#https:// + ://mirror.com + / + files + / + {os} + / + {arch} + / + setup.exe

raw_url = urlunparse(["https", "mirror.com", "files", "os", "arch", "setup.exe"])
print(raw_url)

parsed_url = urlparse(raw_url)
print(parsed_url)