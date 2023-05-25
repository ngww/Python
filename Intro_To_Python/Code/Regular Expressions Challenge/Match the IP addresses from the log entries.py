import re

log_entries = """
user1 GET /endpoint 1.1.1.1 200
user2 POST /endpoint 2.2.2.2 201
user1 PUT /endpoint 3.3.3.3 500
user1 PATCH /endpoint 4.4.4.4 401
"""

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
matches = re.findall(pattern, log_entries)
print(matches)

# Example text to search:
'''
user1 GET /endpoint 1.1.1.1 200
user2 POST /endpoint 2.2.2.2 201
user1 PUT /endpoint 3.3.3.3 500
user1 PATCH /endpoint 4.4.4.4 401
'''

# Should match:
# ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

