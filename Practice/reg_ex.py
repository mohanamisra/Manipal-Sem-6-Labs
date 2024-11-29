import re

text = """
Today's date is 23/1/2024, or more precisely, 23rd November, 2024, or you could say 23-11-2024!
"""

pattern = r"[1-2][0-9]\/1[0-2]?\/[0-2][0-9][0-9][0-9]"

match = re.findall(pattern, text)
print(match)
