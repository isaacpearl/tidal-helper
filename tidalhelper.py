#!/usr/bin/env python
import sys
import os

def test_file_system():
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

def make_folders(d):
    d.sort()
    
    return d 

def main():
    sample_folder = './test_samples'
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            sample_folder = sys.argv[1]
    f = []
    for(dirpath, dirnames, filenames) in os.walk(sample_folder):
        f.extend(filenames)
    sample_folders = make_folders(f)

main()
