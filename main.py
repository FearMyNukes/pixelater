from PIL import Image, ImageStat
from datetime import date

# Object of the image as a whole
img = Image.open('./photos/Scream.jpg')

# Object used to directly address single pixels in the image
px = img.load()

# function whose purpose is to give us the result of our edits
# img is a var of type Image
def getPhoto(img, name):
    today = date.today()
    img.save("./result/{}_{}.jpeg".format(name, today), "JPEG")

# Finds the average color of a block of pixels
# block is a Image object instance
def averageBlock(block):
    height = block.size[0]
    width = block.size[1]
    px = block.load()
    numPixels = height * width

    sumR = 0
    sumG = 0
    sumB = 0

    for i in range(width):
        for j in range(height):
            sumR += px[j, i][0]
            sumG += px[j, i][1]
            sumB += px[j, i][2]

    # Divides the summed RGB values by the total number of pixels 
    # then rounds to two decimals points and returns it in a tuple
    avg = ( int(sumR/numPixels), int(sumG/numPixels), int((sumB/numPixels)))
    return avg

# img:      an Image Object
# section:  subsection of the total Image
# position: tuple location of the top left corner where the block was taken from 
def replaceBlock(img, section, position):
    blockAvg = averageBlock(section)
    newBlock = Image.new(mode="RGB", size=section.size, color=blockAvg)
    img.paste(newBlock, position)
    return img


def pixelize(img, pixelSize, name):
    # get dimensions of the photo
    height = img.size[0]
    width = img.size[1]

    # define a grid of subsections for the image
    x = 0
    y = 0
    while ( y < height ):
        while ( x < width ):
            pos = ( x, y, (x+pixelSize), (y+pixelSize) )
            block = img.crop(pos)
            replaceBlock(img, block, (pos[0], pos[1]) )
            x += pixelSize
        x = 0
        y += pixelSize
    getPhoto(img, name)

pixelize(img, 10, "scream")
