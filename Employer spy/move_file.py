import os

def move_files():
    for file in os.listdir(os.getcwd()):
        filename, file_extension = os.path.splitext(file)
        src = os.getcwd() + '\\' + file

        print(f'Started work on file {filename}, with ext. {file_extension}')
        if file_extension.lower() in ['.png', '.txt']:
            new_destination = os.getcwd() + '\\Spy\\' + file
            os.rename(src, new_destination)

move_files()