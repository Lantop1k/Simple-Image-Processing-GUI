#import libraries
from PIL import ImageOps,Image

#image processing functions
#function to rotate image
def rotate(file):
    img=Image.open(file)  
    return img.rotate(180,expand=1)

#function to convert image to black and white    
def black_and_white(file):
   img=Image.open(file) 
   return img.convert("L")

#function to convert image to mirror    
def mirror(file):
    img=Image.open(file)
    return  ImageOps.mirror(img)

#function to convert image to negative
def negative(file):
     img=Image.open(file)
     return ImageOps.invert(img)
