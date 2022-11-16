// [ 백준 ] 11050번: 이항 계수 1

#include<stdio.h>

int BinomialCoefficient(int n, int r)
{
    int result = 1;
    for (int i = n; i > n - r; i--) {
        result *= i;
    }
    for (int i = 1; i <= r; i++) {
        result /= i;
    }
    return result;
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);
    printf("%d", BinomialCoefficient(N, K));
}
