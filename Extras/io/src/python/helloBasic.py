# Illustrates basic I/O using stdin and stdout. Just echo "Hello " (name) for
# each name in a file.
# Michael Albert 2/2021

import sys

for line in sys.stdin:
	print("Hello " + line.rstrip());

	# The rstrip is needed because each line is newline terminated so just
	# printing would result in blank lines between. Try it and see!