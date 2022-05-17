# MixItUp-Scripts
My Python 3.8.x scripts for MixItUp (Chat bot) app

This is my collection of Python 3.8.x (or higher) scripts created for MixItUp Chat Bot.
I will do my best to keep the scripts commented with how the code works

get_file_list.py
- Requires no additional modules
- Creates a text file listing media files from target folder using the following arguments
-- Usage: <script> "path/to/text/file" "folder/path/to/scan" "list of extensions to add"
-- Example: get_file_list.py "C:\SomeFolder\sfx_file_list.txt" "C:\Folder\containing\sfx\files" ".mp3,.wav"
  
Use "External Program" action to use in MixItUp.
- Program Path should point to python.exe (3.8.x or higher)
- Program Arguments should match Usage/Example above
