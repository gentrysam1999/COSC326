 # Process a file consisting of poems or stanzas of poems separated by blank
 # lines, preceding each by the number of the poem followed by a full stop, 
 # then the number of the line, padding with white space to width 10, then the 
 # line itself. Place one blank line between poems. Number from 1.

import sys

poemNumber = 0

def process(poem):
	global poemNumber
	poemNumber += 1
	lineNumber = 0
	for line in poem:
		lineNumber += 1
		pre = (str(poemNumber) + "." + str(lineNumber) + "          ")[0:10]
		print(pre + line)

poem = []

for line in sys.stdin:
	if (not line.strip()): # Line is empty
		if len(poem) > 0:
			process(poem)
			print()
			poem = []
	else:
		poem.append(line.rstrip())
if len(poem) > 0:
	process(poem)




	