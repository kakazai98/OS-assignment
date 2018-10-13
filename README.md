# OS-assignment

#include <stdio.h>
#include <unistd.h>

int main()
{
		int total[10];

		int fd1[2];
		if (pipe(fd1)==-1)
		{
			printf("Pipe Failed" );
			return 1;
		}

		int a=1,b=101,childvalue,k;
	for(k=0 ; k < 10 ; k = k + 1)		
	{	 

		int childPid;
		childPid = fork();
		if(childPid == 0)
		{
			int x,z;


			int sum = 0,i;
			for(i = a; i<b ; i=i+1)
			{
				sum = sum + i;
			}
			write(fd1[1],&sum,sizeof(int));
			return 0; 
		}
		a=a+100;
		b=b+100;

	}
	close(fd1[1]);
	int l,sum=0; 
	for(l=0 ; l<10 ; l=l+1)
	{
		wait();
		read(fd1[0],&childvalue,sizeof(int));
		sum  =  sum + childvalue;		
	}	

	close(fd1[0]);

	printf("\n SUM OF THE FIRST 1000 NATURAL NUMBERS : %d \n",sum);
}













//..............................................................................................................//






