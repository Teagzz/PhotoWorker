# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:31:30 2018

@author: teagz
"""
import time
import os
import os.path
import shutil
print ("Welcome to the picture organizer!")
print("This program will now create new folders for any repeating filenames.")

folder_path =r"K:\Program Files (x86)\Dropbox (Madore Photography)\Jobs in Progress\1 HDR Finished - To be edited"
images = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
number_files = len(list(os.walk(folder_path)))
time.sleep(2)
print ("Starting organization")
#Takes each picture and assigns its name to a new folder

for image in images:
    #offsets folder name to exclude un needed info
    folder_name = image[:-15]
    
    new_path = os.path.join(folder_path, folder_name)
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    old_image_path = os.path.join(folder_path, image)
    new_image_path = os.path.join(new_path, image)
    shutil.move(old_image_path, new_image_path)

time.sleep(1.5)
print ("Organization, Complete.")
print ("Program finished with:",number_files -1,"folders")
    
    
   
    