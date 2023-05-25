import re

# pattern = r"\b[6-8]\b"
pattern = r'[6-8]'
string = "0987654321234567890"

matches = re.findall(pattern, string)

print(matches)

# Example text to search:
# 0987654321234567890

# Should match:
# ['8', '7', '6', '6', '7', '8'] 

