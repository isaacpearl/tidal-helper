#!/usr/bin/env python
import sys
import os
from shutil import copyfile

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

def organize(files):
    folders = {} #key = prefix, value = list of filenames
    files.sort()
    for i in range(len(files)):
        prefix = files[i].split('_')[0] #assume all files start with desired folder name, then underscore  
        if prefix in folders:
            folders[prefix].append(files[i])
        else:
            folders[prefix] = [files[i]]
    return folders

def create_folder(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def make_folders(path, folders):
    curr_path = path + "tidal_samples/"
    create_folder(curr_path)
    for prefix in folders:
        group_path = curr_path+prefix+'/'
        create_folder(group_path)
        for sample in folders[prefix]:
            #print("path+sample: %s, group_path: %s" % (path+sample, group_path+sample))
            copyfile(path+sample, group_path+sample)

def main():
    samples_path = './test_samples/' #just for early testing
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            samples_path = sys.argv[1]
    f = []
    for(dirpath, dirnames, filenames) in os.walk(samples_path):
        f.extend(filenames)
    folder_info = organize(f)
    make_folders(samples_path, folder_info)
main()
