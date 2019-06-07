#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:00:22 2019
@author: MCA
"""
import os
import string

def loadFiles(subdir, filetype):
    """
    example:
    dirs = ["dir1", "dir2"]
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



#directory = "/.../temp/"
directory = os.path.dirname(os.path.realpath(__file__))+"/"
fileType = ""
names = loadFiles(directory, fileType)

for name in names:
     
    if "112" in name:
      print(name)
      newName = name
      newName = newName.replace("112", "115")
      os.rename(name, newName)
