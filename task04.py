import urllib.parse as url

source = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v5'}

encoded = url.urlencode(source)
print(encoded)
print(url.parse_qs(encoded))

print()

row_str = "k3+k4 r1-v2"
print(url.quote(row_str))       #' ' -> '%20'
print(url.quote_plus(row_str))  #' ' -> '+'