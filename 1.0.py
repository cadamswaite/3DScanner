#Requires PIL - pip install Pillow

angle = 3
pics = int(360/angle)
#or
#pics = 120
#angle = 360/pics

thresh = 200

#ConfigEnd
from PIL import Image
import time
import math
import os
start_time = time.time()

#d1 is the distance from center to edge according to camera
#d2 is the distance between camera and laser
#l2 is the length frim the laser to the center of the object
#radius is length from the center of the object to outside edge
def radworkerouter(d1):
    l2=22*640
    d2=14*640
    radius = (l2*d1)/d2
    return(radius)

def analyse_image(imname,thresh):
    try:
        im = Image.open(imname)
    except:
        print ("Unable to load image")
        exit()
    width, height = im.size
    im = im.crop((0, 0, int(width/2), height)) #Only processes the left side of image
    pixels = im.load()
    width, height = im.size
    all_pixels = []
    for y in range(height):
        for x in range(width):
            cpixel = pixels[x, y]
            r,g,b = cpixel
            if g>thresh: #using a green laser
                added = 0
                while added < 30 and (x+added)<width-1:
                    added = added + 1
                    cpixel = pixels[x+added, y]
                    r,g,b = cpixel
                    if g<thresh:
                        break
                mean = (added-1)/2
                a = [(width-(x+mean)),(height-y)]
                all_pixels.append(a)
                break
    return(all_pixels)

def xyworkerouter(angle,dist):
    y = round(dist*math.cos(math.radians(angle)),2)
    x = round(dist*math.sin(math.radians(angle)),2)
    return(x,y)

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#from random import randint
with open('temp.ply', 'w') as f:
    f.write("")

for pic_angle in range(0,pics):
    imname = str(pic_angle) + ".jpg"
    print(imname)
    pic_angle = pic_angle * angle
    all_pixels = analyse_image(imname,thresh)
    for item in all_pixels:
        dist,z = item
        radius = radworkerouter(dist)
        x, y = xyworkerouter(pic_angle,radius)
        with open('temp.ply', 'a') as f:
            f.write(str(x) + " " + str(y) + " " + str(z) + "\n")

with open('temp.ply', 'r') as f:
    file = f.read()
with open('plot2.ply', 'w') as f:
    f.write("""ply
format ascii 1.0
element vertex """ + str(file_len('temp.ply')) + """
property float x
property float y
property float z
element face 0
property list uchar int vertex_indices
end_header
""" + file)
os.remove('temp.ply')

print (time.time() - start_time, "seconds")
