import time
# Not quite working
path_to_file = "C:\\Users\\jpkee\\Downloads\\TESTFile.txt"
print(path_to_file)
def open_file(path_to_file, attempts=0, timeout=5, sleep_int=5):
    if attempts < timeout and os.path.exists(path_to_file) and os.path.isfile(path_to_file): 
        try:
            file = open(path_to_file)
            return file
        except:
            print('this is the exception part')
            sleep (sleep_int)
            open_file(path_to_file, attempts +10)


# do more here, to basiclly poll the file and if it exists, delete it
import time
fileCounter = 10
while os.path.exists("C:\\Users\\jpkee\\Downloads\\TESTFile.txt"):
    print("file is there")
    time.sleep(2)