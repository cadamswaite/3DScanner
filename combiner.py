from PIL import Image
import plymaker
import xyworkerouter1
import linefinder
import time
import similartri

start_time = time.time()

plymaker.start_it()
angle = 0
thresh = 200


for angle in range(0,120):
    angle = 3*angle
    imname = str(angle)+".jpg"
    print(imname)
    all_pixels = linefinder.analyse_image(imname,thresh)
    for item in all_pixels:
        dist,z = item
        radius = similartri.radworkerouter(dist)
        x, y = xyworkerouter1.xyworkerouter(angle,radius)
        plymaker.plotit(x,y,z)
plymaker.finish_it()

print (time.time() - start_time, "seconds")
