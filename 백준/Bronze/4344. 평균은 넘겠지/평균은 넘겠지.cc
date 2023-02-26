#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, i, j, sum, cnt;
	double avg, per;
	scanf("%d", &n);
	int** test = (int**)malloc(n * sizeof(int*));
	double* percent = (double*)malloc(n * sizeof(double));
	for (i = 0; i < n; i++)
		test[i] = (int*)malloc(1001 * sizeof(int*));

	
	for (i = 0; i < n; i++)
	{
		scanf("%d", &test[i][0]);
		sum = cnt = 0;
		avg = per = 0;
		for (j = 1; j <= test[i][0]; j++)
		{
			scanf("%d", &test[i][j]);
			sum += test[i][j];
		}
		avg = sum / (double)test[i][0];

		for (j = 1; j <= test[i][0]; j++)
			if (test[i][j] > avg) cnt++;

		per = cnt / (double)test[i][0] * 100;
		percent[i] = per;
	}

	for (i = 0; i < n; i++)
		printf("%.3lf%%\n", percent[i]);

	return 0;
	
}