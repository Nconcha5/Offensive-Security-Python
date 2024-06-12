from sys import argv
import os

folder_name = 'Clone'
count = 0

script = sys.argv
main_file_name = os.path.basename(script[0])

try:
    for i in range(10):
        count += 1
        temp = folder_name + str(count)
        os.mkdir(temp)
        shutil.copy(main_file_name, temp)
except Exception as Error:
    print(Error)

count += 10



