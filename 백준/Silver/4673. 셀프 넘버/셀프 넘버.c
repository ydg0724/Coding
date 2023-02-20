#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

    int test[10000], n, d = 0;

    for (int i = 1; i <= 10000; i++) {
        n = i;
        d = n;
        while (n > 0) {
            d += n % 10;
            n /= 10;
        }
        if (d < 10000) {
            test[d] = -1;
        }
        n = 0;
        d = 0;
    }

    for (int j = 1; j < 10000; j++) {
        if (test[j] != -1)
            printf("%d\n", j);
    }

}