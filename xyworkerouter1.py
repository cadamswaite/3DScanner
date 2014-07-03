import math

def xyworkerouter(angle,dist):
    y = round(dist*math.cos(math.radians(angle)),2)
    x = round(dist*math.sin(math.radians(angle)),2)
    return(x,y)
#print(xyworkerouter(45,4))
