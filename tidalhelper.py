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
    folders = {}
    d.sort()
    for i in range(len(d)):
        prefix = d[i].split('_')[0] #assume all files start with desired folder name, then underscore  
        if prefix in folders:
            folders[prefix].append(d[i])
        else:
            folders[prefix] = [d[i]]
    return folders

def main():
    sample_folder = './test_samples' #just for early testing
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            sample_folder = sys.argv[1]
    f = []
    for(dirpath, dirnames, filenames) in os.walk(sample_folder):
        f.extend(filenames)
    sample_folders_dict = make_folders(f)
main()
