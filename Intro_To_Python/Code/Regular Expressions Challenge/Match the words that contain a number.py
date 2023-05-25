import re

words = """space
space1
apple
2apple
brush
brush3"""

pattern = r'\b\w*\d\w*\b'
matches = re.findall(pattern, words)
print(matches)

# Example text to search:
'''
space
space1
apple
2apple
brush
brush3
'''

# Should match:
# ['space1', '2apple', 'brush3']

