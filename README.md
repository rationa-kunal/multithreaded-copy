# multithreaded-copy

copy using pthread library

## How does it work
The code focuses on spliting the file into smaller file and then copying thos file and finally merging those file

## How to get it work
The main c code which does the work is compiled in cp binary
For copying any file you have to execute python file `copy.py` with 3 command line argument that are absolute path of source directory, absolute path of destination directory, filename
for eg
```
python3 copy.py /path/of/sorce/ /path/of/dest/ filename
```
