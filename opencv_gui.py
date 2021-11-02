import cv2
import easygui
from easygui import *
import tkinter as Tk
from tkinter import filedialog
from tkinter import *
import os
import sys
import ast
import datetime
from datetime import datetime

def exit_program():

    warning = "warning.png"
    msg = "Do you want to Quit the Program?"
    title = "Quit Program?"
    choice = buttonbox(msg, title, choices=["Yes", "No"], image=None)
    if choice == "Yes":
        os._exit(0)
    if choice == "No":
        main_program()
 
loop = 0
while(loop==0):
    
    def main_program():
        
        msg = "                          PYTHON OPENCV PITCUTRES MANAGER\n\n     ---------------------------------------------------------------------\n\n            THIS PROGRAM USES THE PYTHON OPENCV LIBRARY, TO EDIT PICTURES\n\n            THESE CAN BE SAVED TO A NEW FILE IF NEEDED\n\n     ---------------------------------------------------------------------\n\n\n                  SUPPORTED IMAGE FILES ARE THE FOLLOWING:\n\n                      .jpg .jpeg .png .bmp .pbm .pgm .ppm\n\n                      .sr .ras .jpe.jp2 .tiff .tif\n\n     ---------------------------------------------------------------------\n\n                  * NOTE: THE CONSOLE ALSO SHOWS DETAILED INFORMATION,\n\n                    ABOUT HOW THE PROGRAM RUNS, AND THE OPERATIONS ON IMAGES YOU\n\n                    EXECUTE                 \n\n\n                    ---> PRESS A BUTTON TO LOAD A PICTURE AN EDIT IT"
        title = "PYTHON OPENCV PICTURES MANAGER"
        Opencv = "opencvpython.png"
        choice = buttonbox(msg=msg, title=title, choices=["Downscale Image", "Upscale Image", "Width Scaling", "Height Scaling", "EXIT PROGRAM"], image=None)
        if choice == "Downscale Image":

            loop = 1
            while(loop==1):

                def downscale_open_file():

                    try:
                        
                        filetypes_list = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.pbm", "*.pgm", "*.ppm", "*.sr", "*.ras", "*.jpe", "*.jp2", "*.tiff", "*.tif"]
                        openfile = easygui.fileopenbox(msg=" Select a supported image", title="File Open", filetypes=filetypes_list, multiple=True)
                            
                        for item in openfile:
     
                            if ".png" in item or ".jpg" in item or ".jpeg" in item or ".bmp" in item or ".pbm" in item or ".pgm" in item or ".ppm" in item or ".sr" in item or ".ras" in item or ".jpe" in item or ".jp2" in item or ".tiff" in item or ".tif" in item:
                                lines = "--------------------------------------------------------"
                                print(lines)
                                print("OPENED IMAGE IN DOWNSCALING MODE")
                                print(lines)
                                print("Loaded image: "+item)
                                
                                img = cv2.imread(item)
                                dimensions = img.shape
                                height = img.shape[0]
                                width = img.shape[1]
                                channels = img.shape[2]
                                pixels = " pixels"
                                print(lines)
                                print('Total Image Dimension    : ',dimensions) 
                                print(lines)
                                print('Image Height       : ',str(height)+pixels)
                                print(lines)
                                print('Image Width        : ',str(width)+pixels)
                                print(lines)
                                print('Number of Channels : ',channels)
                                
                                msg = "Image opened is: "+item+"\n\n"+lines+"\n"+"Total Image Dimension: "+str(dimensions)+"\n"+lines+"\n"+"Height: "+str(height)+" pixels\n"+lines+"\n"+"Width: "+str(width)+" pixels\n"+lines+"\n\nClick OK to view the loaded image with Linux image viewer."
                                title = "OK to view image"
                                msgbox(msg, title, image=None)
                                imageviewerlinux = 'eog '
                                openimage_terminal = os.system(imageviewerlinux+item)
                                loop = 2
                                while(loop==2):

                                    percentagesign = '%'
                                    msg = "Please enter a percentage number to scale the image\n\n------------------------------------------------------------------------\n\nThis percentage number must be less than the total (100%)\n\nExample: Entering 80, will shrink the image to 20%.\n\n------------------------------------------------------------------------\n\n*   Use only integers to scale the image\n\n"
                                    title = "Image Downscaling"
                                    percentage = integerbox(msg, title, default=None, lowerbound=0, upperbound=200)

                                    try:

                                        if percentage > 100:
                                            msg = "A greater value than the total (100%) cannot be entered\n\nClick OK to enter a smaller value"
                                            title = "Limit exceeded"
                                            msgbox(msg, title, image=None)

                                        elif percentage < 100:

                                            img = cv2.imread(item)
                                            dimensions = img.shape
                                            height = img.shape[0]
                                            width = img.shape[1]
                                            channels = img.shape[2]
                                            
                                            width = int(img.shape[1] * int(percentage) / 100)
                                            height = int(img.shape[0] * int(percentage) / 100)
                                            dim = (width, height)
                                            print(lines)
                                            print(lines)
                                            print("IMAGE DOWNSCALING SPECS:")
                                            print(" ")
                                            print("The image downscale percentage value is: "+str(percentage)+percentagesign)
                                            print(lines)
                                            print("It will be resized to: "+str(dim))
                                            print(lines)
                                            print("Height: "+str(height)+pixels)
                                            print(lines)
                                            print("Width: "+str(width)+pixels)
                                            print(lines)

                                            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                            msg = "DOWNSCALING VALUE IS SET TO: "+str(percentage)+percentagesign+"\n"+lines+"\nThe image will be resized with these parameters: "+str(dim)+"\n"+lines+"\n"+"Height: "+str(height)+pixels+"\n"+lines+'\n'+"Width: "+str(width)+pixels+'\n'+lines+"\n\n                 ---> Click OK to show the scaled image"
                                            title = "Downscaling Window"
                                            msgbox(msg, title, image=None)

                                            print("THE IMAGE WAS RESIZED, YOU CAN RIGHT CLICK ON IT TO PERFORM OTHER OPERATIONS.")
                                            print("ONCE YOU CLOSE IT, YOU WILL GET BACK TO THE MAIN MENU")

                                            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                            cv2.imshow("Resized image", resized)
                                            now = datetime.now()
                                            file = item.split("/")
                                            resized_item=(file[-1])
                                            cv2.imwrite(str(now)+"_"+str(resized_item), resized)
                                            cv2.waitKey(0)
                                            cv2.destroyAllWindows()
                                            main_program()

                                    except:
                                        msg = "YOU PRESSED THE CANCEL BUTTON\n\n---------------------------------------------------------------------\n\n---> WHAT WOULD YOU LIKE TO DO?"
                                        title = "Cancel button pressed"
                                        redcross = "redcross.png"
                                        buttons = ["<-- Back to Open file", "<-- Back to Main Menu", "EXIT PROGRAM"]
                                        choice = buttonbox(msg=msg, title=title, choices=buttons, image=None)
                                        if choice == "<-- Back to Open file":
                                            downscale_open_file()
                                        elif choice == "<-- Back to Main Menu":
                                            main_program()
                                        elif choice == "EXIT PROGRAM":
                                            exit_program()

                            else:
                                msg = "   ERROR: YOU MUST OPEN A VALID IMAGE FILE FORMAT TO OPERATE WITH OPENCV\n\n     ---------------------------------------------------------------------\n\n                      SUPPORTED IMAGE FILES ARE THE FOLLOWING:\n\n                      .jpg .jpeg .png .bmp .pbm .pgm .ppm\n\n                      .sr .ras .jpe.jp2 .tiff .tif\n\n     ---------------------------------------------------------------------\n\n\n                        CLICK OK TO RETRY"
                                title = "ERROR, no valid file image opened"
                                redcross = "redcross.png"
                                msgbox(msg=msg, title=title, image=None)
                                height_open_file()
                    except:

                        msg = "                       YOU PRESSED THE CANCEL BUTTON\n\n\n                       ---> CLICK OK TO GET BACK TO MAIN MENU"
                        title = "File open canceled"
                        redcross = "redcross.png"
                        msgbox(msg=msg, title=title, image=None)
                        main_program()


                downscale_open_file()

        if choice == "Upscale Image":

            loop = 3
            while(loop==3):

                def upscale_open_file():

                    try:

                        filetypes_list = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.pbm", "*.pgm", "*.ppm", "*.sr", "*.ras", "*.jpe", "*.jp2", "*.tiff", "*.tif"]
                        openfile = easygui.fileopenbox(msg=" Select a supported image", title="File Open", filetypes=filetypes_list, multiple=True)
                                
                        for item in openfile:

                            if ".png" in item or ".jpg" in item or ".jpeg" in item or ".bmp" in item or ".pbm" in item or ".pgm" in item or ".ppm" in item or ".sr" in item or ".ras" in item or ".jpe" in item or ".jp2" in item or ".tiff" in item or ".tif" in item:
                                lines = "--------------------------------------------------------"
                                print(lines)
                                print("OPENED IMAGE IN UPSCALING MODE")
                                print(lines)
                                print("Loaded image: "+item)
                                
                                img = cv2.imread(item)
                                dimensions = img.shape
                                height = img.shape[0]
                                width = img.shape[1]
                                channels = img.shape[2]
                                pixels = " pixels"
                                print(lines)
                                print('Total Image Dimension    : ',dimensions) 
                                print(lines)
                                print('Image Height       : ',str(height)+pixels)
                                print(lines)
                                print('Image Width        : ',str(width)+pixels)
                                print(lines)
                                print('Number of Channels : ',channels)
                                
                                msg = "Image opened is: "+item+"\n\n"+lines+"\n"+"Total Image Dimension: "+str(dimensions)+"\n"+lines+"\n"+"Height: "+str(height)+" pixels\n"+lines+"\n"+"Width: "+str(width)+" pixels\n"+lines+"\n\nClick OK to view the loaded image with Linux image viewer."
                                title = "OK to view image"
                                msgbox(msg, title, image=None)
                                imageviewerlinux = 'eog '
                                openimage_terminal = os.system(imageviewerlinux+item)
                                loop = 4
                                while(loop==4):

                                    msg = "Please enter a percentage number to scale the image\n\n------------------------------------------------------------------------\n\nExample: To upscale or increase the image size in 20%, enter 20\n\n------------------------------------------------------------------------\n\n*   Use only integers to scale the image\n\n"
                                    title = "Image Upscaling"
                                    percentage = integerbox(msg, title, default=None, lowerbound=0, upperbound=500)

                                    try:

                                        if percentage > 0:
                                            total = 100
                                            percentagesign = '%'
                                            img = cv2.imread(item)
                                            dimensions = img.shape
                                            height = img.shape[0]
                                            width = img.shape[1]
                                            channels = img.shape[2]
                                            increased = total+percentage
                                            width = int(img.shape[1] * int(increased) / 100)
                                            height = int(img.shape[0] * int(increased) / 100)
                                            dim = (width, height)
                                            print(lines)
                                            print(lines)
                                            print("IMAGE UPSCALING SPCES:")
                                            print(" ")
                                            print(lines)                                        
                                            print("Increasing size percentage will be +"+str(percentage)+percentagesign)
                                            print(lines)
                                            print("It will be resized to: "+str(dim))
                                            print(lines)
                                            print("Height: "+str(height)+pixels)
                                            print(lines)
                                            print("Width: "+str(width)+pixels)
                                            print(lines)
                                            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                            msg = "UPSCALING VALUE IS SET TO: +"+str(percentage)+percentagesign+".\n\n"+lines+"\nThe image will be resized with these parameters: "+str(dim)+"\n"+lines+"\n"+"Height: "+str(height)+pixels+"\n"+lines+'\n'+"Width: "+str(width)+pixels+'\n'+lines+"\n\n                 ---> Click OK to show the scaled image"
                                            title = "Upscaling Window"
                                            msgbox(msg, title, image=None)

                                            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                            cv2.imshow("Resized image", resized)
                                            now = datetime.now()
                                            file = item.split("/")
                                            resized_item=(file[-1])
                                            cv2.imwrite(str(now)+"_"+str(resized_item), resized)
                                            cv2.waitKey(0)
                                            cv2.destroyAllWindows()

                                            print("THE IMAGE WAS RESIZED, YOU CAN RIGHT CLICK ON IT TO PERFORM OTHER OPERATIONS.")
                                            print("ONCE YOU CLOSE IT, YOU WILL GET BACK TO THE MAIN MENU")
                                            main_program()

                                    except:

                                        msg = "YOU PRESSED THE CANCEL BUTTON\n\n---------------------------------------------------------------------\n\n---> WHAT WOULD YOU LIKE TO DO?"
                                        title = "Cancel button pressed"
                                        redcross = "redcross.png"
                                        buttons = ["<-- Back to Open file", "<-- Back to Main Menu", "EXIT PROGRAM"]
                                        choice = buttonbox(msg=msg, title=title, choices=buttons, image=None)
                                        if choice == "<-- Back to Open file":
                                            upscale_open_file()
                                        elif choice == "<-- Back to Main Menu":
                                            main_program()
                                        elif choice == "EXIT PROGRAM":
                                            warning = "warning.png"
                                            msg = "Do you want to Quit the Program?"
                                            title = "Quit Program?"
                                            choice = buttonbox(msg, title, choices=["Yes", "No"], image=None)
                                            if choice == "Yes":
                                                os._exit(0)
                                            if choice == "No":
                                                upscale_open_file()
                            else:
                                msg = "   ERROR: YOU MUST OPEN A VALID IMAGE FILE FORMAT TO OPERATE WITH OPENCV\n\n     ---------------------------------------------------------------------\n\n                      SUPPORTED IMAGE FILES ARE THE FOLLOWING:\n\n                      .jpg .jpeg .png .bmp .pbm .pgm .ppm\n\n                      .sr .ras .jpe.jp2 .tiff .tif\n\n     ---------------------------------------------------------------------\n\n\n                        CLICK OK TO RETRY"
                                title = "ERROR, no valid file image opened"
                                redcross = "redcross.png"
                                msgbox(msg=msg, title=title, image=None)
                                upscale_open_file()
                    
                    except:
                        msg = "                       YOU PRESSED THE CANCEL BUTTON\n\n\n                       ---> CLICK OK TO GET BACK TO MAIN MENU"
                        title = "File open canceled"
                        redcross = "redcross.png"
                        msgbox(msg=msg, title=title, image=None)
                        main_program()


                upscale_open_file()
        
        if choice == "Width Scaling":

            loop = 5
            while(loop==5):

                    def width_open_file():

                        try:

                            global filetypes_list, openfile
                            filetypes_list = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.pbm", "*.pgm", "*.ppm", "*.sr", "*.ras", "*.jpe", "*.jp2", "*.tiff", "*.tif"]
                            openfile = easygui.fileopenbox(msg=" Select a supported image", title="File Open", filetypes=filetypes_list, multiple=True)
                                
                        
                            for item in openfile:

                                        
                                    if ".png" in item or ".jpg" in item or ".jpeg" in item or ".bmp" in item or ".pbm" in item or ".pgm" in item or ".ppm" in item or ".sr" in item or ".ras" in item or ".jpe" in item or ".jp2" in item or ".tiff" in item or ".tif" in item:
                                        lines = "--------------------------------------------------------"
                                        print(lines)
                                        print("OPENED IMAGE IN WIDTH SCALING MODE")
                                        print(lines)
                                        print("Loaded image: "+item)
                                        
                                        img = cv2.imread(item)
                                        dimensions = img.shape
                                        height = img.shape[0]
                                        width = img.shape[1]
                                        channels = img.shape[2]
                                        pixels = " pixels"
                                        print(lines)
                                        print('Total Image Dimension    : ',dimensions) 
                                        print(lines)
                                        print('Image Height       : ',str(height)+pixels)
                                        print(lines)
                                        print('Image Width        : ',str(width)+pixels)
                                        print(lines)
                                        print('Number of Channels : ',channels)
                                        
                                        msg = "Image opened is: "+item+"\n\n"+lines+"\n"+"Total Image Dimension: "+str(dimensions)+"\n"+lines+"\n"+"Height: "+str(height)+" pixels\n"+lines+"\n"+"Width: "+str(width)+" pixels\n"+lines+"\n\nClick OK to view the loaded image with Linux image viewer."
                                        title = "OK to view image"
                                        msgbox(msg, title, image=None)
                                        imageviewerlinux = 'eog '
                                        openimage_terminal = os.system(imageviewerlinux+item)
                                        loop = 6
                                        while(loop==6):

                                            msg = "Please enter a number to scale the Width of the image\n\n------------------------------------------------------------------------\n\n*   Use only integers to scale the image\n\n"
                                            title = "Width Scaling"
                                            Width = integerbox(msg, title, default=None, lowerbound=0, upperbound=150000)

                                            try:

                                                if Width < 2:
                                                    msg = "A value smalled than the total 2 cannot be entered\n\nClick OK to enter a greater value"
                                                    title = "Limit exceeded"
                                                    msgbox(msg, title, image=None)
                                                    
                                                elif Width > 2:
                                                    
                                                    img = cv2.imread(item)
                                                    dimensions = img.shape
                                                    height = img.shape[0] # keep original height
                                                    dim = (width, height)
                                                    
                                                    # resize image
                                                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                                    
                                                    print(lines)
                                                    print(lines)
                                                    print("WIDTH UPSCALING SPCES:")
                                                    print(" ")
                                                    print("The Width scaling value is: "+str(Width))
                                                    print(lines)

                                                    Width_size = str(Width-width)
                                                    #Width_size_result = ast.literal_eval(Width_size_bigger)
                                                                                    
                                                    print("It will be resized to: "+str(height)+", "+str(Width))
                                                    print(lines)
                                                    print("Height: "+str(height)+pixels)
                                                    print(lines)
                                                    print("Width: "+str(Width)+pixels)
                                                    print(lines)
                    
                                                    msg = "WIDTH SCALING VALUE IS SET TO: "+str(Width)+'\n'+lines+"\n"+"The image will be resized with these parameters: "+str(height)+","+str(Width)+"\n"+lines+"\n"+"Height: "+str(height)+pixels+"\n"+lines+'\n'+"Width: "+str(Width)+pixels+'\n'+lines+"\n"+"Returned Width Increment or Decrment value is: "+str(Width_size)+" pixels\n\n                 ---> Click OK to show the scaled image"
                                                    title = "Width Scaling Window"
                                                    msgbox(msg, title, image=None)

                                                    width = Width
                                                    dim = (Width, height)
                                                    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                                    cv2.imshow("Resized image", resized)
                                                    now = datetime.now()
                                                    file = item.split("/")
                                                    resized_item=(file[-1])
                                                    cv2.imwrite(str(now)+"_"+str(resized_item), resized)
                                                    cv2.waitKey(0)
                                                    cv2.destroyAllWindows()
                                                    main_program()

                                            except:

                                                        msg = "YOU PRESSED THE CANCEL BUTTON\n\n---------------------------------------------------------------------\n\n---> WHAT WOULD YOU LIKE TO DO?"
                                                        title = "Cancel button pressed"
                                                        redcross = "redcross.png"
                                                        buttons = ["<-- Back to Open file", "<-- Back to Main Menu", "EXIT PROGRAM"]
                                                        choice = buttonbox(msg=msg, title=title, choices=buttons, image=None)
                                                        if choice == "<-- Back to Open file":
                                                            width_open_file()
                                                        elif choice == "<-- Back to Main Menu":
                                                            main_program()
                                                        elif choice == "EXIT PROGRAM":
                                                            os._exit(0)

                                                                                                         

                                    else:
                                        msg = "   ERROR: YOU MUST OPEN A VALID IMAGE FILE FORMAT TO OPERATE WITH OPENCV\n\n     ---------------------------------------------------------------------\n\n                      SUPPORTED IMAGE FILES ARE THE FOLLOWING:\n\n                      .jpg .jpeg .png .bmp .pbm .pgm .ppm\n\n                      .sr .ras .jpe.jp2 .tiff .tif\n\n     ---------------------------------------------------------------------\n\n\n                        CLICK OK TO RETRY"
                                        title = "ERROR, no valid file image opened"
                                        redcross = "redcross.png"
                                        msgbox(msg=msg, title=title, image=None)
                                        width_open_file() 
                
                        
                        except:
                            msg = "                       YOU PRESSED THE CANCEL BUTTON\n\n\n                       ---> CLICK OK TO GET BACK TO MAIN MENU"
                            title = "File open canceled"
                            redcross = "redcross.png"
                            msgbox(msg=msg, title=title, image=None)
                            main_program()
            
                    width_open_file()

        if choice == "Height Scaling":

            loop = 7
            while (loop==7):

                def height_open_file():

                    try:

                        filetypes_list = ["*.png", "*.jpg", "*.jpeg", "*.bmp", "*.pbm", "*.pgm", "*.ppm", "*.sr", "*.ras", "*.jpe", "*.jp2", "*.tiff", "*.tif"]
                        openfile = easygui.fileopenbox(msg=" Select a supported image", title="File Open", filetypes=filetypes_list, multiple=True)
                                
                        for item in openfile:

                                    
                                if ".png" in item or ".jpg" in item or ".jpeg" in item or ".bmp" in item or ".pbm" in item or ".pgm" in item or ".ppm" in item or ".sr" in item or ".ras" in item or ".jpe" in item or ".jp2" in item or ".tiff" in item or ".tif" in item:
                                    lines = "--------------------------------------------------------"
                                    print(lines)
                                    print("OPENED IMAGE IN HEIGHT SCALING MODE")
                                    print(lines)
                                    print("Loaded image: "+item)
                                    img = cv2.imread(item)
                                    dimensions = img.shape
                                    height = img.shape[0]
                                    width = img.shape[1]
                                    channels = img.shape[2]
                                    pixels = " pixels"
                                    print(lines)
                                    print('Total Image Dimension    : ',dimensions) 
                                    print(lines)
                                    print('Image Height       : ',str(height)+pixels)
                                    print(lines)
                                    print('Image Width        : ',str(width)+pixels)
                                    print(lines)
                                    print('Number of Channels : ',channels)
                                    
                                    msg = "Image opened is: "+item+"\n\n"+lines+"\n"+"Total Image Dimension: "+str(dimensions)+"\n"+lines+"\n"+"Height: "+str(height)+" pixels\n"+lines+"\n"+"Width: "+str(width)+" pixels\n"+lines+"\n\nClick OK to view the loaded image with Linux image viewer."
                                    title = "OK to view image"
                                    msgbox(msg, title, image=None)
                                    imageviewerlinux = 'eog '
                                    openimage_terminal = os.system(imageviewerlinux+item)
                                    
                                    loop = 8
                                    while(loop==8):                                

                                        msg = "Please enter a number to scale the Height of the image\n\n------------------------------------------------------------------------\n\n*   Use only integers to scale the image\n\n"
                                        title = "Height Scaling"
                                        Height = integerbox(msg, title, default=None, lowerbound=0, upperbound=150000)

                                        try:

                                            if Height < 2:
                                                msg = "A value smalled than the total 2 cannot be entered\n\nClick OK to enter a greater value"
                                                title = "Limit exceeded"
                                                msgbox(msg, title, image=None)
                                                
                                            elif Height > 2:
                                                
                                                img = cv2.imread(item)
                                                dimensions = img.shape
                                                height = img.shape[0] # keep original height
                                                dim = (width, Height)
                                                
                                                # resize image
                                                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                                
                                                print(lines)
                                                print(lines)
                                                print("HEIGHT UPSCALING SPCES:")
                                                print(" ")
                                                print("The Height scaling value is: "+str(Height))
                                                print(lines)
                                                height_difference = str(Height-height)
                                                print("Difference amount between original Height, and set value is: "+str(height_difference)+pixels)
                                                print(lines)
                                                print("It will be resized to: "+str(Height)+","+str(width))
                                                print(lines)
                                                print("Height: "+str(Height)+pixels)
                                                print(lines)
                                                print("Width: "+str(width)+pixels)
                                                print(lines)

                                                msg = "HEIGHT SCALING VALUE IS SET TO: "+str(Height)+".\n\n"+lines+"\n"+"\nThe image will be resized with these parameters: "+str(Height)+", "+str(width)+"\n"+lines+"\n"+"Height: "+str(Height)+pixels+"\n"+lines+'\n'+"Width: "+str(width)+pixels+'\n'+lines+"\n"+"Returned Height increment or decrement value is: "+str(height_difference)+"\n"+lines+"\n\n                 ---> Click OK to show the scaled image"
                                                title = "Height Scaling Window"
                                                msgbox(msg, title, image=None)
                                                
                                                dim = (width, Height)
                                                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

                                                height = Height
                                                dim = (width, height)
                                                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                                                cv2.imshow("Resized image", resized)
                                                now = datetime.now()
                                                file = item.split("/")
                                                resized_item=(file[-1])
                                                cv2.imwrite(str(now)+"_"+str(resized_item), resized)
                                                cv2.waitKey(0)
                                                cv2.destroyAllWindows()

                                                print("THE IMAGE WAS RESIZED, YOU CAN RIGHT CLICK ON IT TO PERFORM OTHER OPERATIONS.")
                                                print("ONCE YOU CLOSE IT, YOU WILL GET BACK TO THE MAIN MENU")
                                                main_program()

                                        except:
                                                msg = "YOU PRESSED THE CANCEL BUTTON\n\n---------------------------------------------------------------------\n\n---> WHAT WOULD YOU LIKE TO DO?"
                                                title = "Cancel button pressed"
                                                redcross = "redcross.png"
                                                buttons = ["<-- Back to Open file", "<-- Back to Main Menu", "EXIT PROGRAM"]
                                                choice = buttonbox(msg=msg, title=title, choices=buttons, image=None)
                                                if choice == "<-- Back to Open file":
                                                    height_open_file()
                                                elif choice == "<-- Back to Main Menu":
                                                    main_program()
                                                elif choice == "EXIT PROGRAM":
                                                    warning = "warning.png"
                                                    msg = "Do you want to Quit the Program?"
                                                    title = "Quit Program?"
                                                    choice = buttonbox(msg, title, choices=["Yes", "No"], image=None)
                                                    if choice == "Yes":
                                                        os._exit(0)
                                                    if choice == "No":
                                                        height_open_file()

                                else:
                                    msg = "   ERROR: YOU MUST OPEN A VALID IMAGE FILE FORMAT TO OPERATE WITH OPENCV\n\n     ---------------------------------------------------------------------\n\n                      SUPPORTED IMAGE FILES ARE THE FOLLOWING:\n\n                      .jpg .jpeg .png .bmp .pbm .pgm .ppm\n\n                      .sr .ras .jpe.jp2 .tiff .tif\n\n     ---------------------------------------------------------------------\n\n\n                        CLICK OK TO RETRY"
                                    title = "ERROR, no valid file image opened"
                                    redcross = "redcross.png"
                                    msgbox(msg=msg, title=title, image=None)
                                    height_open_file()


                    except:
                            msg = "                       YOU PRESSED THE CANCEL BUTTON\n\n\n                       ---> CLICK OK TO GET BACK TO MAIN MENU"
                            title = "File open canceled"
                            redcross = "redcross.png"
                            msgbox(msg=msg, title=title, image=None)
                            main_program()


                height_open_file()

        if choice == "EXIT PROGRAM":
            exit_program()
    main_program()
