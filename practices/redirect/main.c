#include <stdio.h>
#include "redirect_ptr.h"

int main(void){

	const char *p1=NULL;
	const char *p2=NULL;
	get_a_day(&p1);
	get_a_day(&p2);
	printf("%s\t%s\n",p1,p2);
	return 0;
}

