import sys
import re
import requests

if len(sys.argv) != 2:
    print("Usage: pyport <file>")
    exit()

with open(sys.argv[1], 'r') as f:
    contents = f.readlines()

for idx, line in enumerate(contents):
    import_http = re.match(r'from "(.*?)" import \*', line)
    if import_http:
        url = import_http.group(1)
        file_name = url.split('/')[-1].replace('-', '_')
        file_contents = requests.get(import_http.group(1)).text
        with open(file_name, "w") as f:
            f.write(file_contents)
        contents[idx] = f'from {file_name[:-3]} import *\n'

exec(''.join(contents))
