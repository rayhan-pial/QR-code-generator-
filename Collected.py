#! /usr/bin/python3

import qrcode # Import QR Code library with pip install qrcode[pil]
import sys #To exit the program if QR data is not given
import os #To create the save folder if not already there
from PIL import Image, ImageDraw, ImageFont #Save and display the image
import time #For the waiting

# Prompt user for the data that you want to store, the filename, desired size, and format of the QR code image:
print('===============================================')

multiple = input('Press enter to save as single QR code (default), 1 for Multiple  ')
print('===============================================')
data = input('What info do you want in your QR code: ')
#if len(str(data)) == 0:
 #   print('You did not enter anything.  Exiting Program...')
  #  sys.exit()
#print('===============================================')
#qrLabel = input('Do you want a caption? (Leave blank for no caption) ')
#print('===============================================')
#qrName = input('What do you want to name the QR code file? ')
#print('===============================================')



doCaption = 1
fontFile = 'fonts/FreeMono.ttf'
fontName = 'FreeMono.ttf'
if len(str(qrLabel)) == 0:
    doCaption = 0
else:
    if len(str(qrLabel)) > 24:
        #Removed for now
        print('We are doing a caption.')
        #qrLabel = qrLabel[0:24]
        #print('Truncating your caption to make it fit.')

if len(str(qrName)) == 0:
    print('You did not pick a filename.  Using "myQr" as the filename.')
    print('===============================================')
    qrName = 'myQR'


#Set the image type:
imageExt = '.png'

#Make a folder for saved QRcodes
if not os.path.exists('savefolder'):
    os.makedirs('savefolder')
    print('Creating subfolder: "savefolder"')
    print('===============================================')


if len(str(multiple)) == 1:
    data = input('What info do you want in your QR code: ')
    if len(str(data)) == 0:
        print('You did not enter anything.  Exiting Program...')
        sys.exit()
    
    k=int(input("Total number - "))
    if len(str(k)) == 0:
        print('You did not enter anything.  Exiting Program...')
        sys.exit()
    Item_num= int (input("Number strting from = "))
    if len(str(Item_num)) == 0:
        print('You did not enter anything.  Exiting Program...')
        sys.exit()
    
    qrName == data

        
    qrLabel = input('Do you want a caption? (Leave blank for no caption) ')
    print('===============================================')
        
    for item in range(k):
        #Check to see if we already have a previously created file with the same name:
        if os.path.exists('savefolder/' + str(qrName) + imageExt):
            print('You already have a code named ' + qrName + '. I am renaming it ' + qrName + '-COPY')
            print('===============================================')
            qrName = qrName + '-COPY'

        # Create qr code instance
        qr = qrcode.QRCode()

        # Add data
        #qr.box_size = int(boxPixels)
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        #Are we adding a caption?
        if doCaption:
            draw = ImageDraw.Draw(img)
            QRwidth, QRheight = img.size
            fontSize = 1 #starting font size
            img_fraction = 0.90 # portion of image width you want text width to be, I've had good luck with .90
            fontHeightMax = qr.border * qr.box_size - 10
            captionX = 0
            captionY = 0
            #print('Font height max is set to: ' + str(fontHeightMax))
            font = ImageFont.truetype(fontFile, fontSize)
            while font.getsize(qrLabel)[0] < img_fraction*QRwidth and font.getsize(qrLabel)[1] < fontHeightMax:
                fontSize += 1
                font = ImageFont.truetype(fontFile, fontSize)
            captionX = int(QRwidth - font.getsize(qrLabel)[0]) / 2 #Center the label
            #print('Offset: ' + str(captionX))
            draw.text((captionX, captionY), qrLabel, font=font)

        # Save it somewhere, change the extension as needed:
        img.save("savefolder/" + str(qrName) + imageExt)
        print('QR Code successfully save as ' + str(qrName) + imageExt)
