#include <stdio.h>

int main()
{
	int n, a, b, c, d, sum, cnt = 0;
	do {
	scanf("%d", &n);
	} while (n < 0 || n > 99);
	a = n;

	while (1)
	{
		if (a >=10 || a==0)
			{
			b = a / 10; //십의 자리 수
			c = a % 10;	//일의 자리 수 
			d = (b + c) % 10;
			sum = 10 * c + d;
			cnt++;
			if (n == sum) break;
			a = sum;
			}
		else
		{
			a = a * 10 + a;
			cnt++;
			if (n == a) break;
		}
	}
	printf("%d", cnt);
	
	return 0;

}