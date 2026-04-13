from urllib.parse import urlparse

def parse(url):
    parsedUrl = urlparse(url)
    return {
        'scheme': parsedUrl.scheme,
        'netloc': parsedUrl.netloc,
        'path': parsedUrl.path,
        'params': parsedUrl.params,
        'query': parsedUrl.query,
        'fragment': parsedUrl.fragment,
    }

print(parse("https://user@example.com"))