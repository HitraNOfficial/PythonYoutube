import sys
from os import path
import re

# Unicode symbols
semicolon = u'\u003b'
greekQmark = u'\u037e'

file_name = path.abspath('Main.java')
if (not path.exists(file_name)) or path.islink(file_name):
	print(f'\n{file_name} is not a valid file.')
	sys.exit()
else:
	destroyFile = open(file_name, 'r+', encoding="utf-8")

	# Replace the characters in contents
	contents = destroyFile.read()
	contents = re.sub(semicolon, greekQmark, contents)

	# Overwrite on the original file
	destroyFile.seek(0, 0)
	destroyFile.write(contents)
	destroyFile.close()
	print(f'\nDestroyed file: {file_name}')
