import os
import os.path

ext_path = r"K:\Program Files (x86)\Dropbox (Madore Photography)\Jobs in Progress\Exteriors"
intor_path = r"K:\Program Files (x86)\Dropbox (Madore Photography)\Jobs in Progress\Interiors"
drn_path = r"K:\Program Files (x86)\Dropbox (Madore Photography)\Jobs in Progress\Drone"

def filecount(x):
    count = len([f for f in os.listdir(x)])
    return count

if filecount(drn_path) % 3 ==0:
    print ("Ready to render Drone")
    print(filecount(drn_path) / 3, "Drone Photos Ready to Render")
elif filecount(drn_path) == 0:
    print("There is no Drone Photos to render")
else:
    print ("Drone is not ready to render")
if filecount(ext_path) % 3 ==0:
    print("Ready to render Exteriors")
    print(filecount(ext_path) / 3, "Exterior Photos Ready to Render")
elif filecount(ext_path) == 0:
    print("There are no exteriors to render")
else:
    print("Exteriors are not renderable")
if filecount(intor_path) % 3 == 0:
    print("Ready to render Interiors")

    print(filecount(intor_path) // 3, "Interior Photos Ready to Render")
elif filecount(intor_path) == 0:
    print("There are no Interior photos to render")
else:
    print("Interiors are not renderable")






