#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<pthread.h>
 
 
void* sum(void* value) 
{  
    int start = ((int)value*100)+1;
    int end = start + 100;
    int Partial_sum = 0,i; 
  
    for (i = start; i < end; i++) 
        Partial_sum = Partial_sum + i;
    
    return ((void*)Partial_sum);
} 

int main()
{
    int i;
    int j;
    int Sum=0;
    int answer;

    pthread_t threads[10];

   for (i=0; i < 10; i++)
   {
       pthread_create(&threads[i],NULL,sum,(void*)i);
   }

    for (j = 0; j < 10; j++)
    {
       pthread_join(threads[j],(void**) & answer);
       Sum = Sum + answer;
    }


    printf("\nThe sum of integers from 1-1000 is %d\n\n", Sum);

    return 0;
}
