# MixItUp-Scripts
My Python 3.8.x scripts for MixItUp (Chat bot) app

This is my collection of Python 3.8.x (or higher) scripts created for MixItUp Chat Bot.
I will do my best to keep the scripts commented with how the code works


## Scripts currently available:
###get_file_list.py
- Requires no additional modules
- Creates a text file listing media files from target folder using the following arguments
-- Usage: <script> "path/to/text/file" "folder/path/to/scan" "list of extensions to add"
-- Example: get_file_list.py "C:\SomeFolder\sfx_file_list.txt" "C:\Folder\containing\sfx\files" ".mp3,.wav"
  
Use "External Program" action to use in MixItUp.
- Program Path should point to python.exe (3.8.x or higher)
- Program Arguments should match Usage/Example above
- Make sure "Wait until complete" is checked

###### Notes on get_file_list:
  I have this added to "Events > Generic > Application Launch" to generate the list when MixItUp launches



###get_video_duration.py
- Requires OpenCV2 and MediaInfo modules
  Installing/Upgrading on Windows: (Python 3.8.x)
    python -m pip install --upgrade opencv-python
    python -m pip install --upgrade pymediainfo
- "Quickly" parses a video file to find its duration in seconds, and prints it to stdout for MixItUp
-- Usage: <script> "path/to/video"
-- Example: get_video_duration.py "/some/path/to/video.mp4"
  
Uses "External Program" action in MixItUp
- Program Path should again point to python.exe (3.8.x or higher)
- Program Arguments should match Usage/Example above
- Make sure "Wait Until Complete" is checked
- Make sure "Save Output" is also checked, duration will be saved into $externalprogramresult
