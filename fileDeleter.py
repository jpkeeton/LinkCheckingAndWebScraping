# https://www.w3schools.com/python/python_file_remove.asp
# import os
# testfilePath = "C:\\Users\\jpkee\\Documents\\DELETEME.txt"
# print('printing file path: ' + testfilePath)
# if os.path.exists(testfilePath):
#     print('Found the file and will delete it')
#     # os.remove(testfilePath)
# else:
#     print("Can't find the file")
# # # filepath
# C:\Users\jpkee\Documents
# file
# DELETEME.txt


# import os, sys
# # os.chdir("C:\\tmp")

# os.chdir("C:\\Users\\jpkee\\Desktop\\PythonProjects")

# # C:\Users\jpkee\Desktop\MotionX_GPX_Files

# # C:\Users\jpkee\Desktop\MotionX_GPX_Files

# # listing directories
# print ("The dir is: %s" %os.listdir(os.getcwd()))


# Walking a directory

# import os
# for root, dirs, files in os.walk("C:\\Users\\jpkee\\Desktop\\PythonProjects"):
#     for file in files:
#         if file.endswith(".py"):
#             #  print(os.path.join(root, file))
#             print(len(file))


# HERE ARE SOME TIPS ON MAKING SURE PATHS EXIST
# https://stackabuse.com/python-check-if-a-file-or-directory-exists/


import os
import glob
pythonPath = "C:\\Users\\jpkee\\Desktop\\PythonProjects"
dataPath = "C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasources"

# Python File Variables
jupyterFiles = len(glob.glob1(pythonPath,"*.ipynb"))
regularPythonFiles = len(glob.glob1(pythonPath,"*.py"))

# Data File Variables
excelFiles = len(glob.glob1(dataPath,"*.xlsx"))
csvFiles = len(glob.glob1(dataPath,"*.csv"))

# Check for valid filepath(s)
# print('Checking file paths for: ' + pythonPath + ' and ' +  dataPath + ' are valid')
if os.path.exists(pythonPath):
    print('Python path is valid, so here goes the count!')
# put the counter here
# so put this inside the conditional
# Show how many Python-type files 
    print('There are : ' + str(jupyterFiles) + ' Jupyter files')
    print('There are : ' + str(regularPythonFiles)+ ' regular Python files\n')
else:
    print("Help I'm lost!")

# If the data path is valid, count the files there
if os.path.exists(dataPath):
    print('Data path is valid, so we\'ll count these as well!')
# put the counter here
# so put this inside the conditional
# Show how many Python-type files 
    print('There are : ' + str(csvFiles) + ' CSV Files')
    print('There are : ' + str(excelFiles)+ ' Excel Files\n')
else:
    print("Help I'm lost!")





import os.path
from os import path

def main():

#    print ("File exists:"+str(path.exists('guru99.txt')))
#    Stick this in here:
#     C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasources
   print ("File exists:"+str(path.exists('C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasourcest')))
#    print ("File exists:" + str(path.exists('career.guru99.txt')))
#    print ("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()