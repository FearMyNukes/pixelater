from PIL import Image
from datetime import date

# intialize Image object
IMG = Image.open('./photos/Scream.png')

# Saves photo to filesystem
def getPhoto(img, name):
    today = date.today()
    img.save("./result/{}_{}.png".format(name, today), "PNG")

### Finds the average color of a block of pixels ###

# block: an Image object instance
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
    # then converts to int and returns it in a tuple
    avg = ( int(sumR/numPixels), int(sumG/numPixels), int((sumB/numPixels)))
    return avg

### Function to create an image object using the avg color 
# of pixels then replace the block in the original image ###

# img:      an Image Object
# block:  subsection of the total Image
# position: tuple location of the top left corner where the block was taken from 
def replaceBlock(img, block, position):
    blockAvg = averageBlock(block)
    newBlock = Image.new(mode="RGBA", size=block.size, color=blockAvg)
    img.paste(newBlock, position)
    return img

### function which divides the image passed into a grid then
#  calls the replaceBlock function to create a pixelation effect ###

# img:       an Image Object
# name:      name you want to associate with the file when save will also save with the date
# pixelSize: length of each size of the square to be averaged
def pixelize(img, pixelSize):
    # get dimensions of the photo
    height = img.size[1]
    width = img.size[0]

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
    return img

# pixelize(IMG, "scream", 50)
gifIMGS = [IMG]
i = 5
while (i < 200):
    gifIMGS.append( pixelize(IMG, i) )
    newimg = pixelize(IMG, i)
    # getPhoto(newimg, i)
    i += 50

# print(gifIMGS)
print(len(gifIMGS))
print(gifIMGS[1:])
gifIMGS[0].save('Scream.gif', save_all=True, append_images=gifIMGS[1:], optimize=False, duration=250, loop=0)