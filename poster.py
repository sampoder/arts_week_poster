from PIL import Image
import os
import math 
import glob

files = next(os.walk("img"))[2] #dir is your directory path as string

amountsquares = math.sqrt(len(files)-1)

directory = os.fsencode("/img")

files = []
    
for filepath in glob.iglob('img/*.jpg'):
    files.append(filepath)

for filepath in glob.iglob('img/*.png'):
    files.append(filepath)

i = amountsquares

x = 0
actualresult = Image.new('RGB', (2500, 3500))
while i > 0:
    result = Image.new('RGB', (2500, 350))
    b = amountsquares
    while b > 0:

        image1 = Image.open(files[x])

        (width1, height1) = image1.size


        if height1 > width1:

            nearest_multiple_width = 5 * round(width1/5)

            if nearest_multiple_width >  width1:
                nearest_multiple_width-=5

            amountChanged = nearest_multiple_width/5

            nearest_multiple_height = 7 * amountChanged
            
            xx = 0

            im = image1.crop((((width1-nearest_multiple_width)/2), ((height1-nearest_multiple_height)/2), width1-((width1-nearest_multiple_width)/2), height1-((height1-nearest_multiple_height)/2)))

        else:

            nearest_multiple_height = 7 * round(height1/7)

            if nearest_multiple_height >  height1:
                nearest_multiple_height-=7

            amountChanged = nearest_multiple_height/7

            nearest_multiple_width = 5 * amountChanged

            xx = 1

            im = image1.crop((((width1-nearest_multiple_width)/2), ((height1-nearest_multiple_height)/2), width1-((width1-nearest_multiple_width)/2), height1-((height1-nearest_multiple_height)/2)))

         

        im1 = im.resize((250, 350), Image.ANTIALIAS)

        print(image1.size)
        print(im.size)
        print(im1.size)
        print(nearest_multiple_height)
        print(height1-((height1-nearest_multiple_height)/2))
        result.paste(im=im1, box=(int(250*(10-b)),0))
        b-=1
        x+=1
    
    actualresult.paste(im=result, box=(0,int(350*(10-i))))
    i-=1

background = actualresult
foreground = Image.open("overlay.png")

background.paste(foreground, (0, 0), foreground)
background.show()
