#Базовый URL: //example.com/path/
#Относительные ссылки:
#file.txt
#../other.html
##anchor

import urllib.parse as url

def convert(base, relative):
    result = []
    for el in relative:
        result.append(url.urljoin(base, el))
    return result

base_url = "//example.com/path/"
relative_url = ["file.txt", "../other.html", "#anchor"]
print(convert(base_url, relative_url))