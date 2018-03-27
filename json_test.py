import json
from pprint import pprint

# Read in the file
with open('data.json', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace(',\\', ',')
filedata = filedata.replace(',', ',\n')
filedata = filedata.replace('}},','}},\n')
# Write the file out again
with open('data.json', 'w') as file:
  file.write(filedata)
