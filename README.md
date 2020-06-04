# Opencv Image Editor
Python/linux program to edit picture files, which uses opencv library

Program developed on June 4th, 2020 - Author: Gustavo Wydler Azuaga
-----------------------------------------------------------------------------------------------------

To view sample screenshots of the program, access the Screenshots folder
-----------------------------------------------------------------------------------------------------

Features and how it works:

It consists of 4 buttons, to perform different operations on pictures, modifying the amount of pixels:

   - Downscale Image ---> Shrinks the total image size, accepting only a percentage value less than it´s total, which is                               100%.
   
   - Upscale Image ---> Increases the total image size, when given a percentage value.
   
   - Width Scaling ---> Scales up or down the width of the image, depending on the provided Value. If the value is greater                           than the original width size, it will increase the size, otherwise, it will be decreased.
   
   - Height Scaling ---> Runs the same operation explained for width, but for the height.
   
-----------------------------------------------------------------------------------------------------
*NOTE: The program uses the eog (eye of gnome) imageviewer, so it should be run in a linux system
       with this installed and an operational gnome-terminal as well. You can freely modify this in the code, 
       to run it in another OS.
          
To run the program:

  - Clone the repo
  - Install and import the following python libraries:
    
    - import cv2
    - import easygui
    - from easygui import *
    - import os
    - import sys
    
  - Access the downloaded or cloned folder
  - Open a gnome-terminal and run:
      
      - python3.x opencv_gui.py
  
