# Creating and removing files and directories with Python os module

"""This is done with the os module, which has lots of methods for handling files and dirs"""

import os # this line will import os module

# Make a new file.
# Simply opening a file in write mode will create it at specified location, if it doesn't exist. ( If file does exist,
# the act of opening
# it in write mode will completely overwrite its contents.)

try:
    f = open("file.txt", "w") # It will create file.txt in current location
except IOError as e:
    print(e.errno)
    print(e)

# Remove a file
try:
    os.remove("file.txt")
except os.error as e:
    print(e.errno)
    print(e)

# Make a directory
os.mkdir('dirname')

# Recursive directory creation: creates die_c and if necessary dir_b and dir_a
os.mkdir('dir_a/dir_b/dir_c')

# Remove an empty directory
os.rmdir('dirname')
os.rmdir('dir_a/dir_b/dir_c') # Removes dir_c only



######################################################################################################33

# Create a directory and set user:group with python's os module

import pwd

file_path = 'example'
if not os.path.exists(file_path):
    os.makedirs(file_path)  # Creates with default permission of 0777
    uid, gid = pwd.getpwnam('root').pw_uid, pwd.getpwnam('avi').pw_uid
    os.chown(file_path, uid, gid)  # set user:group as root:avi
