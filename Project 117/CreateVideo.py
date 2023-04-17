import os
import cv2

path = "Images/"
Images = []
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])

if vid.isOpened( == False):
    print("Unable to read the video.")
Height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(Height)
Width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(Width)
FPS = int(vid.get(cv2.CAP_PROP_FPS))
print(FPS)
size = (Width, Height)
print(size)
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'),0.8, size)
for i in range(0, count-1):
    cv2.imread()
    out.write()
print("~~~~~~Done~~~~~~")