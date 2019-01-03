#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>


struct flow_path {
	char *from;
	char *to;
};


void copy_file(struct flow_path *ff){
	FILE *ffrom, *fto;
	// printf("in thread %s\n", ff->from);

	ffrom = fopen(ff->from, "rb");
	if (ffrom == NULL) {
		perror("file open for reading");
		exit(EXIT_FAILURE);
	}
	fto = fopen(ff->to, "wb");
	if (fto == NULL) {
		perror("file open for writing");
		exit(EXIT_FAILURE);
	}

	size_t n, m;
	unsigned char buff[8192];
	do {
		n = fread(buff, 1, sizeof buff, ffrom);
		if (n) m = fwrite(buff, 1, n, fto);
		else   m = 0;
	} while ((n > 0) && (n == m));
	if (m) perror("copy");

}


int main(int argc, char * argv[]){
	if(argc < 3){
		return -1;
	}

	int total_files = (argc-1)/2;

	pthread_t threads[total_files];

	for(int f=1, tid=0; f<argc-1; f+=2, tid++){
		// printf("%d %d %s->%s\n", tid, f, argv[f], argv[f+1]);
		struct flow_path *ff;
		ff = malloc(sizeof(*ff));
		ff->from = argv[f];
		ff->to = argv[f+1];
		int succ = pthread_create(&threads[tid], NULL, (void *) copy_file, ff);
		// printf("t %d\n", succ);
	}

	for(int tid=0; tid<total_files; tid++) pthread_join(threads[tid], NULL);


	return 0;
}