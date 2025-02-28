// https://rosalind.info/problems/kmp/

#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#define HEAD_LEN 100
#define SEQ_LEN 100000

int main(int argc, char *argv[])
{
	FILE *single_fasta = fopen(argv[1], "r");
	
	char head[HEAD_LEN + 1];
	char seq[SEQ_LEN + 1];

	fgets(head, sizeof(head), single_fasta);
	
	int seq_len = 0;
	int line_len;
	char line[SEQ_LEN + 1];

	while((fgets(line, sizeof(seq), single_fasta)) != NULL){

		line[strcspn(line, "\n")] = 0;

		line_len = strlen(line);

		strcpy(seq + seq_len, line);
        seq_len += line_len;
	}

	seq[seq_len + 1] = '\0';
	fclose(single_fasta);

	int length = 0;
	int failure[strlen(seq)];
	failure[0] = 0;

	for(int k = 1; k <= strlen(seq); ){
		if (seq[k] == seq[length]){
			length += 1; 
			failure[k] = length;
			k++;
		}
		else {
			if (length != 0) {
				length = failure[length - 1];
			}
			else {
				failure[k] = 0;
				k++;
			}
		}
	}

	for(int index = 0; index < sizeof(failure)/sizeof(int); index++){
		printf("%d ", failure[index]);
	}
	printf("\n");

	return 0;
}
