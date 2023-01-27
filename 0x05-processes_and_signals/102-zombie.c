#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - function that sleeps indefinitely
 *
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

int main(void)
{
	int i;
	pid_t zombie[5];

	for (i = 0; i < 5; i++)
	{
		zombie[i] = fork();
		if (zombie[i] == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	infinite_while();
	return (0);
}
