import re

f = open("markdown.md", "r")

content = f.read()

content = re.sub(r'(__|\*\*)(.*?)\1', r'<b>\2</b>', content)
content = re.sub(r'[_\*](.*?)\1', r'<i>\2</i>', content)

print(content)

f.close()

