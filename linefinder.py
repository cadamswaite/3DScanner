from PIL import Image

def analyse_image(imname,thresh):
    try:
        im = Image.open(imname)
    except:
        print ("Unable to load image")
        exit()
    width, height = im.size
    im = im.crop((0, 0, int(width/2), height))
    pixels = im.load()
    width, height = im.size
    all_pixels = []
    for y in range(height):
        for x in range(width):
            cpixel = pixels[x, y]
            r,g,b = cpixel
            if g>thresh:
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
