// 2739번: 구구단

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= 9; i++) {
        print("%d * %d = %d\n", N, i, N * i);
    }
}
