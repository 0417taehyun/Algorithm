// [ 백준 ] 2845번: 파티가 끝나고 난 뒤

#include <stdio.h>

void PrintDifference(int L, int P)
{
    int real = L * P;
    int guess;
    while (scanf("%d", &guess) == 1) {
        printf("%d ", guess - real);
    }
}

int main(void)
{
    int L, P;
    scanf("%d %d", &L, &P);
    PrintDifference(L, P);
}