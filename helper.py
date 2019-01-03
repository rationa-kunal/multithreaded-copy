import os
import sys
from subprocess import call

def cmd_split(file, size, prefix):
	print("dividing source file")
	cmd = "split -b " + size + " " + file + " " + prefix
	os.system(cmd)	

def call_copy(f):
	print("copying temp files")
	call(['./cp', *f])

def create_file(path, filename):
	print("creating new file from temp files")
	cmd = "touch " + path + filename
	os.system(cmd)

def combine(file, to, prefix):
	print("combining temp files")
	cmd = "cat "+ to + prefix +"* > " + to + file
	os.system(cmd)

def remove_files(src, prefix):
	print("removing tempfile from", src)
	cmd = "rm "+ src + prefix +"*"
	os.system(cmd)