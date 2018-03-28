import json
from pprint import pprint
import sys
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.")
	
	random.seed()
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
