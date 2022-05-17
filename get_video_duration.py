#!/usr/bin/env python

#---------------------------------------------------
# "Quick" script to get a video duration as seconds
# Rounded up & +1 second, for MixItUp app/bot
# Written for Python 3.8.x
#---------------------------------------------------


#-----------------
# Module imports
#-----------------
# For parsing arguments
import sys

# Preferred video parser
import cv2

# Used if OpenCV fails, though it is clunky
#  and sometimes unreliable
from pymediainfo import MediaInfo

# To round up the video duration (in seconds)
from math import ceil


#---------------------------------------
# The function that does the bulk work
#---------------------------------------
def getDuration(in_vid):
  # Create video capture object
    data = cv2.VideoCapture(r'{}'.format(in_vid))
  # Make sure we were able to open the video
    if data.isOpened():
      # count the number of frames
        frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = int(data.get(cv2.CAP_PROP_FPS))
  # If OpenCV fails to open the video, fallback to MediaInfo
    else:
        media = MediaInfo.parse(r'{}'.format(in_vid))
        for track in media.tracks:
            if track.track_type == 'Video':
                frames = int(track.frame_count)
                fps = float(track.frame_rate)
  # calculate duration of the video
    seconds = frames / fps
    return ceil(seconds)+1


#---------------------------------------
# Main funtion to run if the script is
# run by itself and not imported
#---------------------------------------
def runMainApp():
    if (len(sys.argv)-1) == 1:
        print(getDuration(sys.argv[1]))
  # This will silently fail if neither OpenCV or MediaInfo can read the file


#---------------------------------------
# If the script is run by itself we run
# the function "runMainApp"
#---------------------------------------
if __name__ == '__main__':
    runMainApp()