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


import glob
myPath = "C:\\Users\\jpkee\\Desktop\\PythonProjects"
jupyterFiles = len(glob.glob1(myPath,"*.ipynb"))
regularPythonFiles = len(glob.glob1(myPath,"*.py"))

# print('There are : ' +  jupyterFiles + ' Jupyter files')
# print('There are : ' + regularPythonFiles + ' regular Python files')

print('There are : ' + str(jupyterFiles) + ' Jupyter files')
print('There are : ' + str(regularPythonFiles)+ ' regular Python files')


# print( "Alireza" + str(1980))