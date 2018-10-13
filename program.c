#include <stdio.h>
int main () {

   int a;
int status = 0;
   /* for loop execution */
   for( a = 0; a < 4; a = a + 1 ){
	fork();
      printf("HELLO1 \n");

   }
	wait();
	printf("EXITING PROCESS\n");

   return 0;
}
