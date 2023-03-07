#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a, b, c, result;
	int be, af;
	int cnt[10] = { 0 };

	scanf("%d %d %d", &a, &b, &c);

	result = a * b * c;

	while (result != 0)
	{
		be = result;
		result /= 10;
		af = be - result*10;
		cnt[af]++;
	}
	for (int i = 0; i < 10; i++)
	{
		printf("%d\n", cnt[i]);
	}

	return 0;
}