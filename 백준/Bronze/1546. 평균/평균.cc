#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, i, max;
	double average, sum = 0;

	scanf("%d", &n);
	double* a = (double*)malloc(n * sizeof(double));

	for (i = 0; i < n; i++)
	{
		scanf("%lf", &a[i]);
	}
	max = a[0];

	for (i = 1; i < n; i++)
	{
		if (max < a[i]) max = a[i];
	}
	for (i = 0; i < n; i++)
	{
		a[i] = a[i] / max * 100;
		sum += a[i];
	}
	average = sum / (double)n;

	printf("%lf", average);
	return 0;
}