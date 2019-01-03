import os
import sys
from helper import cmd_split, call_copy, create_file, combine, remove_files
from subprocess import call


PREFIX = "temp_copy_"
COPY = "cp"
TEMP_SIZE = "100MB"
FROM = None
TO = None
FILE = None


# getting command line arg
if len(sys.argv) is 4:
	FROM = sys.argv[1]
	TO = sys.argv[2]
	FILE = sys.argv[3]
else:
	print("No source or destination provided")
	exit()


# dividing source file call to split
cmd_split(file=FROM+FILE, size=TEMP_SIZE, prefix=PREFIX)


# ls
dir = FROM
files = os.listdir(dir)
ffiles = []
for f in files:
	if PREFIX in f:
		ffiles.append(f) 
		ffiles.append(TO+f)
print(len(ffiles), "temporary files created")


# copy temp files from FROM to TOs
call_copy(f=ffiles)


# create new file
create_file(path=TO, filename=FILE)


# combine files
combine(file=FILE, to=TO, prefix=PREFIX)


# removing temp files
remove_files(src=FROM, prefix=PREFIX)
remove_files(src=TO, prefix=PREFIX)

