#!/usr/bin/env python
import sys
import os
from shutil import copyfile

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

def create_directory(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

def make_folders(path, folders):
    curr_path = path + "tidal_samples/"
    create_directory(curr_path)
    for prefix in folders:
        group_path = curr_path+prefix+'/'
        create_directory(group_path)
        for sample in folders[prefix]:
            copyfile(path+sample, group_path+sample)

def main():
    samples_path = ""
    if len(sys.argv) > 1:
        if os.path.isdir(sys.argv[1]):
            samples_path = sys.argv[1]
        else:
            print("Argument was not a valid directory. Exiting tidalhelper ~")
            exit()
    else:
        print("No arguments. Exiting tidalhelper ~")
        exit()
    f = []
    for(dirpath, dirnames, filenames) in os.walk(samples_path):
        f.extend(filenames)
    folder_info = organize(f)
    make_folders(samples_path, folder_info)

main()
