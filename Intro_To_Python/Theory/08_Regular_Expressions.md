# Regular Expressions
Regular expressions, often referred to as regex or regexp, are a powerful tool for pattern matching and manipulation of text. Python provides a built-in module called `re` that allows you to work with regular expressions. Here are some commonly used functions and patterns in Python's regular expression module:

1. **re.match(pattern, string)**: Tests if the pattern matches at the beginning of the string.

```python
import re

pattern = r"abc"
string = "abcdef"
match = re.match(pattern, string)
if match:
    print("Match found!")
else:
    print("No match found.")
```

2. **re.search(pattern, string)**: Searches for a pattern anywhere in the string.

```python
import re

pattern = r"world"
string = "Hello, world!"
match = re.search(pattern, string)
if match:
    print("Match found!")
else:
    print("No match found.")
```

3. **re.findall(pattern, string)**: Returns all non-overlapping occurrences of the pattern in the string as a list.

```python
import re

pattern = r"\d+"
string = "I have 10 apples and 5 oranges."
matches = re.findall(pattern, string)
print(matches)  # Output: ['10', '5']
```

4. **re.sub(pattern, repl, string)**: Substitutes all occurrences of the pattern in the string with the replacement string.

```python
import re

pattern = r"apple"
string = "I have an apple and another apple."
replacement = "orange"
new_string = re.sub(pattern, replacement, string)
print(new_string)  # Output: "I have an orange and another orange."
```

5. **Metacharacters**:
   - `.` (dot): Matches any character except a newline.
   - `*`: Matches zero or more occurrences of the preceding character.
   - `+`: Matches one or more occurrences of the preceding character.
   - `?`: Matches zero or one occurrence of the preceding character.
   - `^`: Matches the start of a string.
   - `$`: Matches the end of a string.
   - `[]`: Matches any single character within the brackets.
   - `|`: Matches either the expression before or after the pipe symbol.
   - `()` (parentheses): Groups a subpattern.

These are just a few examples of what you can do with regular expressions in Python. The `re` module provides many more functions and features for advanced pattern matching and manipulation. You can refer to the Python documentation for a comprehensive guide to regular expressions in Python.

## Examples
Here are some examples of how you can use regular expressions in Python:

1. Matching a specific pattern:

```python
import re

pattern = r"apple"
string = "I have an apple."
match = re.match(pattern, string)
if match:
    print("Match found!")
else:
    print("No match found.")
```

2. Extracting numbers from a string:

```python
import re

pattern = r"\d+"
string = "I have 10 apples and 5 oranges."
matches = re.findall(pattern, string)
print(matches)  # Output: ['10', '5']
```

3. Splitting a string based on a pattern:

```python
import re

pattern = r"\s+"
string = "Hello   World   !"
words = re.split(pattern, string)
print(words)  # Output: ['Hello', 'World', '!']
```

4. Finding email addresses in a text:

```python
import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
text = "Contact me at john@example.com or jane@example.org"
emails = re.findall(pattern, text)
print(emails)  # Output: ['john@example.com', 'jane@example.org']
```

5. Removing punctuation from a string:

```python
import re

pattern = r"[^\w\s]"
string = "Hello, World!"
clean_string = re.sub(pattern, "", string)
print(clean_string)  # Output: "Hello World"
```

These examples demonstrate the basic usage of regular expressions in Python. You can modify the patterns and strings to suit your specific needs and use cases. Remember to use the `r` prefix before the pattern string to indicate a raw string, which helps in avoiding unintended escape characters.

## Lookarounds
Lookarounds are advanced features in regular expressions that allow you to specify conditions before or after a pattern without including them in the actual match. Python's `re` module supports two types of lookarounds: positive lookaheads and negative lookaheads.

1. Positive Lookahead (?=pattern):
   - Matches the current position if followed by the pattern.
   - It does not consume any characters in the string.
   - Example: Matching a word that is followed by "apple".

```python
import re

pattern = r"\w+(?=\sapple)"
string = "I have a red apple."
match = re.search(pattern, string)
if match:
    print("Match found:", match.group())  # Output: "red"
```

2. Negative Lookahead (?!pattern):
   - Matches the current position if not followed by the pattern.
   - It does not consume any characters in the string.
   - Example: Matching a word that is not followed by "apple".

```python
import re

pattern = r"\w+(?!\sapple)"
string = "I have a red apple and a green apple."
matches = re.findall(pattern, string)
print(matches)  # Output: ['I', 'have', 'a', 'and', 'a', 'green']
```

3. Positive Lookbehind (?<=pattern):
   - Matches the current position if preceded by the pattern.
   - It does not consume any characters in the string.
   - Example: Matching a word that is preceded by "red".

```python
import re

pattern = r"(?<=red\s)\w+"
string = "I have a red apple and a red car."
matches = re.findall(pattern, string)
print(matches)  # Output: ['apple']
```

4. Negative Lookbehind (?<!pattern):
   - Matches the current position if not preceded by the pattern.
   - It does not consume any characters in the string.
   - Example: Matching a word that is not preceded by "red".

```python
import re

pattern = r"(?<!red\s)\w+"
string = "I have a red apple and a green car."
matches = re.findall(pattern, string)
print(matches)  # Output: ['I', 'have', 'a', 'apple', 'and', 'a', 'green', 'car.']
```

Lookarounds are powerful tools for more precise pattern matching and can be combined with other regular expression features to achieve complex matching requirements. Remember that lookarounds do not consume characters, so they only assert conditions without actually including them in the matched result.