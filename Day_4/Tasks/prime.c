#include <stdio.h>
/**
 * main - The main program that decides whether a number is prime or not
 *
 * Return: 0
 */
int main(void)
{
	int n, i;

	/* Get the user's input*/
	printf("Enter the number: ");
	scanf("%d", &n);

	/* Loop for all the numbers less than n and bigger than 2*/
	i = n - 1;
	while (i > 2)
	{
		if (n % i == 0)
		{
			printf("The number \"%d\" is not a prime number", n);
			return (0);
		}
		i--;
	}
	printf("The number \"%d\" is a prime number", n);

	return (0);
}
