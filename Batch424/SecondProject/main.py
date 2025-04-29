"""
read    r       
write   w
append  a
extensive x
w   =  override the current content if file exists othervise write in new file
r   =  read
a   =  append the current file if file exists othervise work as 'w'
w+  =  same as 'w' + 'r'
r+  =  same as 'w' + 'r'
a+  =  same as 'a' + 'r'
x   =  first check if the file is exists then throws error else same as 'w'
x+  =  same as 'x' + 'r'
"""

# file_obj = open("first.txt",'a+')
# file_obj.write("Hello Universe")
# print(file_obj.read())
# file_obj.close()

with open('first.txt','w+') as file:
    file.write('hello ')
    file.write("here this is still open")
    print(file.tell())
    file.seek(0,2)            # moves to the end
    file.seek(0,1)            # shows current position 
    file.seek(0,0)            # moves to the start
    file.seek(12,0)            # moves to the 12th step a head 
    position = file.tell()    # gives current position
    print(position)
    print(file.read())

import time
with open('second.txt','w') as file:
    file.writelines(['hello world\n','hello universe\n'])
    file.flush()
    time.sleep(0)
    file.writelines(['hello another world\n','hello multiverse\n'])

with open('second.txt')as file:
    # print(file.read())               # read whole content
    # print(file.readline())           # reads single line
    # print(file.readline())      
    print(file.readlines())           # reads whole content and divide lines inside list element


def table(num):
    for i in range(1,11,1):            # 1 2 3 4 5 6 7 8 9 10
        yield f'{num} X {i} = {num*i}\n'


num = int(input("Enter Number for table :"))         #4
with open('table.txt','w') as file:
    file.writelines(list(table(num)))
    # print(file.writable())
    # print(file.readable)


num = int(input("Enter Number for table1 :"))         #4
with open('table1.txt','w') as file:
    for i in range(1,11,1):
        file.write(f'{num} X {i} = {num*i}\n')



print(list(table(4)))