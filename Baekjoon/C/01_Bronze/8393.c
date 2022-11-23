// [ 백준 ] 8393번: 합

#include <stdio.h>

int CalculateSum(int number)
{
    return (number * (number + 1)) / 2;
}

int main(void)
{
    int n;
    scanf("%d", &n);
    printf("%d", CalculateSum(n));
}