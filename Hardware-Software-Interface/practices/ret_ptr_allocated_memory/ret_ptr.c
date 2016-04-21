#include <string.h>
#include "ret_ptr.h"

static const char *msg[]={"Sunday","Monday","Tuesday"};

char *get_a_day(int idx){

	static char buf[20];
	// write to the same memory allocation since address
	// &buf do not change during the function call
	strcpy(buf,msg[idx]);
	return buf;
}