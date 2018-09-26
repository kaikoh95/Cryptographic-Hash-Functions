#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char** argv)
{
	if (argc < 4)
	{
		printf("Usage: Comparer ByteCount File1 File2\n");
		return 0;
	}
	int length;
	int fd1, fd2;
	int read1, read2;
	length = atoi(argv[1]);

	char *file1 = (char *)malloc(length);
	char *file2 = (char *)malloc(length);

	
	fd1 = open(argv[2], O_RDONLY);
	fd2 = open(argv[3], O_RDONLY);
	if (fd1 <0 || fd2 <0)
	{
		printf("Failed to open files\n");
		return 0;
	}

	read1 = read(fd1, file1, length);
	read2 = read(fd2, file2, length);
	if(read1 < length || read2 < length)
	{
		printf("Failed to read in files\n");
		return 0;
	}
	
	int different = 0;
	int i, j;
	for(i=0;i<length;i++)
	{
		char pointer = 0x01;
		for(j=0;j<8;j++)
		{
			if((file1[i]&pointer) != (file2[i]&pointer))
				different++;
			pointer = pointer<<1;
		}
	}
	printf("Comparer:\n    %d bits different between %s and %s in first %d byte(s)\n", different, argv[2], argv[3], length);
	return 0;
}
