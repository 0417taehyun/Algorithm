// [ 백준 ] 15964번: 이상한 기호

#include <stdio.h>

long long calculator(long long x, long long y)
{
    return (x+y)*(x-y);
}

int main(void)
{
    long long A, B;
    scanf("%lld %lld", &A, &B);
    printf("%lld", calculator(A, B));

}