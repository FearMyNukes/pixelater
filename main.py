from PIL import Image, ImageStat
from datetime import date

# Object of the image as a whole
img = Image.open('./photos/beachBall.jpeg')
# Object used to directly address single pixels in the image
px = img.load()

# print(img.format, img.size, img.mode)

# img.show()


# Convert the image to RGB or 8 bit
# center of pixel on (0,0) is (0.5,0.5)

# imgStats = ImageStat.Stat(img, mask=None)
# print(imgStats.mean)


# function whose purpose is to give us the result of our edits
# img is a var of type Image
def getPhoto(img, name):
    today = date.today()
    img.save("{}{}.jpeg".format(name, today), "JPEG")

def pixelize(img, pixelSize):
    # get dimensions of the photo
    height = img.size[0]
    width = img.size[1]

    # define a grid of subsections for the image

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
    return ( round((sumR/numPixels), 2), round((sumG/numPixels), 2), round((sumB/numPixels), 2))

averageBlock(img)
# pixelize(img)
# box = (100, 100, 400, 400)
# region = im.crop(box)
# code to create a crop of the photo



# region = region.transpose(Image.Transpose.ROTATE_180)
# im.paste(region, box)