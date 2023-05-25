import re

pattern = r'https?://([A-Za-z_0-9.-]+)'
url = 'https://cloudacademy.com'
match = re.search(pattern, url)
if match:
    domain = match.group(1)
    print(domain)

# Example text to search:
# 'https://cloudacademy.com'

# Should match:
# ['cloudacademy.com']

