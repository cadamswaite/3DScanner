#d1 is the distance from center to edge according to camera
#d2 is the distance between camera and laser
#l2 is the length frim the laser to the center of the object
#radius is length from the center of the object to outside edge
def radworkerouter(d1):
    l2=22*640
    d2=14*640
    radius = (l2*d1)/d2
    return(radius)

