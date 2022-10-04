import fileinput
import re

urls = []

pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]))+'

for i in fileinput.input('input.txt'):
    if re.search(pattern, i):
        findUrl = re.findall(pattern, i)
        urls.append(findUrl)

with open("output.txt","w") as file:
    for u in range (len(urls)):
        lineText = '\n'.join(urls[u])
        print (lineText)
        file.write(lineText)
        