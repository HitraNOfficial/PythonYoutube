from os import path
import re

semicolon = u'\u003b'
greekQmark = u'\u037e'

file_name = path.abspath('Main.java')

destroy_file = open(file_name, 'r+', encoding='utf-8')

contents = destroy_file.read()
contents = re.sub(semicolon, greekQmark, contents)

destroy_file.seek(0, 0)
destroy_file.write(contents)
destroy_file.close()
print(f'\nDestroyed file: {file_name}')