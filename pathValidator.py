import os.path
from os import path
import glob

def main():

#    print ("File exists:"+str(path.exists('guru99.txt')))
#    Stick this in here:
#     C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasources
#    print ("File exists:"+str(path.exists('C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasources')))
#    print ("File exists:" + str(path.exists('career.guru99.txt')))
      print ("directory exists:" + str(path.exists('C:\\Users\\jpkee\\Documents\\My Tableau Repository\\Datasources')))

pythonPath = "C:\\Users\\jpkee\\Desktop\\PythonProjects"
regularPythonFiles = len(glob.glob1(pythonPath,"*.py"))

if os.path.exists(pythonPath):
    print('Python path is valid, so here goes the count!')
    print('There are : ' + str(regularPythonFiles)+ ' regular Python files\n')
else:
    print("Help I'm lost!")

if __name__== "__main__":
   main()
