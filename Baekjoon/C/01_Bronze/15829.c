// [ 백준 ] 15829번: Hashing

#include <stdio.h>
#include <string.h>

const int MOD = 1234567891;
const int BASE = 31;
const char CHARACTER_START = 'a';

int main(void)
{
    int N;
    char S[51];
    scanf("%d %s", &N, &S);

    long long sum = 0;
    long long r = 1;
    for (int i = 0; i < strlen(S); i++)
    {
        int c = (S[i] - CHARACTER_START + 1) % MOD;
        r = r % MOD;
        sum += ((c * r) % MOD);
        r *= BASE;
    }
    printf("%lld", sum % MOD);
}