#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:00:22 2019

@author: MCA
"""
import os

def loadFiles(subdir, filetype):
    """
    example:
    dirs = ["iter_threads0", "iter_threads4"]

    file_type = ".dat"

    files, keys, data = loadFiles(dirs[0], file_type)
    
    """    
    
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, (subdir+"/"))
    files_path = []
    fileNamesFiltered = []
    for root, dirs, files in os.walk(path):  
        for i, filename in enumerate(files):
            if filename[(len(filename))-len(filetype):] == filetype:
#                print(filename)
                filename_path = path + filename
                files_path.append(filename_path)
                fileNamesFiltered.append(filename)
                  
    
    return fileNamesFiltered



directory = "/folder/folder2/"
fileType = ".txt"
names = loadFiles(directory, fileType)

for name in names:
    print("#       "+name+" xxx")
