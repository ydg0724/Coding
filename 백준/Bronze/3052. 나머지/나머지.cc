#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int i, cnt = 0,n;
	int a[42] = { 0 };

	for (i = 0; i < 10; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < 42; j++)
		{
			if (n % 42 == j)
			{
				a[j] = 1;
				break;
			}
		}
	}

	for (i = 0; i < 42; i++)
	{
		if (a[i] == 1) cnt++;
	}

	printf("%d", cnt);

	
	return 0;
}