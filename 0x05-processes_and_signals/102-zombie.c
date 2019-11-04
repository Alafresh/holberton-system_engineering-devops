#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 * Return: 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create zombie process
 * Return: nothing
 */

int main(void)
{
	int count;
	pid_t zombie;

	count = 0;
	while (count < 5)
	{
		zombie = fork();
		if (zombie == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", zombie);
		}
		count++;
	}
	infinite_while();
return (0);
}
