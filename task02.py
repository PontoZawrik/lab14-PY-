import urllib.parse as url

row_url = "http://example.com?special=!@#$%^&*()_+"
parsed_url = url.urlparse(row_url)
print(url.parse_qsl(parsed_url.query))
print(url.parse_qs(parsed_url.query))