#include <stdio.h>

int main(void){

	int array[4]={1,2,3,4};
	printf("%d is at address %p \n", *(array+1), array+1);
	// printf("= %d \n", array[0]);
	// printf(array);
	printf("Initial address of the array is %p \n", array);
	return 0;	
}