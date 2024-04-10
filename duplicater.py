from sys import argv
import os

folder_name = 'Clone'

count = 0

script = argv
main_file_name = str(script[0])

for i in range(10):
    count += 1
    temp = folder_name +str(count)
    os.mkdir(temp)
    os.system(r"copy " + main_file_name +" {0}".format(temp))

except Exception as Error:
print(Error)
count += 10

