import sys

for line in sys.stdin:
	name = line.strip();
	if name: # Python trick - empty strings are 'false'
		print("Hello " + name);

	