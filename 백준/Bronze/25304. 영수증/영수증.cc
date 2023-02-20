#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int price,total;
	int a, b;
	int sum=0;
	scanf("%d %d", &price, &total);
	for (int i = 0; i < total; i++)
	{
		scanf("%d %d", &a, &b);
		sum += a * b;
	}
	
	if (price == sum) printf("Yes");
	else printf("No");

	return 0;
	
}