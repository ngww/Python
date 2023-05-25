import re

pattern = r'(?<!\S)(?:[^\so]*o){0,2}[^o\s]*(?!\S)'
string = 'hop hoop hooop hoooop hooooop'

matches = re.findall(pattern, string)

print(matches)

# Example text to search:
# 'hop hoop hooop hoooop hooooop'

# Should match:
# ['hop', 'hoop']
