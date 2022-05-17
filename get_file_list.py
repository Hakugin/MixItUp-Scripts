#!/usr/bin/env python

#---------------------------------------------------
# Simple Script to crawl SFX directory
# List of SFX files are then written to text file
#  for MixItUp chat bot, written for Python 3.8.x
#---------------------------------------------------
# List File Location    : sys.argv[1]
# Video File Location   : sys.argv[2]
# Extensions to catalog : sys.argv[3]
#---------------------------------------------------


#-----------------
# Module imports
#-----------------
# For parsing arguments
import sys
# For working with file/folder paths
from pathlib import Path



#---------------------------------------------------
# Check for an existing list file
#---------------------------------------------------
def checkExistingFile(sfx_list, list_file):
  # Making sure the file exists
    if Path(list_file).exists():
      # Open the file
        with open(list_file, 'r') as in_file:
          # Iterate through the file
            for x in in_file:
              # Ignore blank lines
                if x.rstrip() != '':
                  # Add filepath to sfx_list
                    sfx_list.add('{}'.format(x.rstrip()))

#---------------------------------------------------
# Scan the target folder for desired extensions
#---------------------------------------------------
def getFolderFileList(sfx_list, scan_folder, scan_exts):
  # Walk the target directory
    for path in Path(r'{}'.format(scan_folder)).glob(r'**/*'):
      # Check if file found has desired extension
        if path.suffix in scan_exts:
          # Add the file to the sfx_list
            sfx_list.add('{}'.format(path))

#---------------------------------------------------
# Save the compiled list to the file, overwrites
#---------------------------------------------------
def saveListToFile(sfx_list, list_file):
  # Open the target text file
    with open(list_file, 'w') as out_file:
      # Iterate through the sfx_list
        for x in sfx_list:
          # Ignore possible blank entries
            if x != '' and Path(x).exists():
              # Write filepath to the text file
                out_file.write('{}\r\n'.format(x))

#---------------------------------------------------
# Function run when script is run, not imported
#---------------------------------------------------
def runMainApp():
  # Create a set, only stores unique values
    SFX_LIST = set()
  # Assign first 2 script arguments appropriately
    LIST_FILE, SCAN_FOLDER = sys.argv[1],sys.argv[2]
  # Split the third argument and assign it
    EXTENSIONS = sys.argv[3].split(',')

  # Run through each function with the correct objects
    checkExistingFile(SFX_LIST, LIST_FILE)
    getFolderFileList(SFX_LIST,SCAN_FOLDER,EXTENSIONS)
    saveListToFile(SFX_LIST,LIST_FILE)

  # Done, let script caller know
    return


#---------------------------------------------------
# Confirm whether script was run or imported
#---------------------------------------------------
if __name__ == '__main__':
    runMainApp()