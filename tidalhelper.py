#!/usr/bin/env python
import sys
import os

def main():
    path = os.getcwd()

    if os.path.isdir(sys.argv[1]):
        print('argument is a directory')
    else:
        print('argument is not a directory')

    new_folder_path = path+'/testfolder'

    for arg in sys.argv:
        print('arg: %s', arg)

    try:
        os.mkdir(new_folder_path)
    except OSError:
        print('creation of directory %s failed', new_folder_path)
    else:
        print('successfully created directory %s', new_folder_path)

main()
