// [ 백준 ] 2609번: 최대공약수와 최소공배수

#include <stdio.h>

int FindGreatestCommonDivisor(int a, int b)
{
    int result = 0;
    int maximum = a;
    if (a > b) {
        maximum = b;
    }
    for (int i = 1; i <= maximum; i++) {
        if ((a % i == 0) && (b % i == 0)) {
            result = i;
        }
    }
    return result;
}

int FindLeastCommonMultiple(int a, int b, int gcd)
{
    return a * b / gcd;
}


int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);
    int gcd = FindGreatestCommonDivisor(a, b);
    int lcm = FindLeastCommonMultiple(a, b, gcd);
    printf("%d\n%d", gcd, lcm);
}
