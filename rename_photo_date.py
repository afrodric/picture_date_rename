#!/usr/bin/python -tt
# 
# 
# 

"""
This program

1 obtain a list of pictures (jpg & JPG) at current directory


2 load a each picture on the list and obtain the taken_date 


3 create a file with the commands to rename pictures


4 
"""

import sys
import glob
from PIL import Image


def obtainTakenDate (filename):
  return Image.open(filename)._getexif()[36867].replace(":", "_")
  



# Define a main() function .
def main():
  # Obtain a list of JPG and jpg files.
  photoFiles = []
  photoFiles = photoFiles + glob.glob("*.JPG")
  photoFiles = photoFiles + glob.glob("*.jpg")
  for photoFile in photoFiles :
    newLine = "mv "+ photoFile + "  " + obtainTakenDate(photoFile).replace(" ", "_") + ".jpg"
    print newLine


# Standard call to the main() function.
if __name__ == '__main__':
  main()
