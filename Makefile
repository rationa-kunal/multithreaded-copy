compile: copy_function.c
	gcc -std=c11 -pthread -o cp copy_function.c

delete: cp
	rm cp
