#include <stdio.h>

int main()
{
    int a,b;
    int mul1, mul2, mul3, mul4;
    scanf("%d%d", &a,&b);

    mul1 = a * (b % 10);
    mul2 = a * ((b % 100) / 10);
    mul3 = a * (b / 100);
    mul4 = a * b;

    printf("%d\n%d\n%d\n%d", mul1, mul2, mul3, mul4);

    return 0;
}