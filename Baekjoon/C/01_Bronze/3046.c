// [ 백준 ] 3046번: R2

#include <stdio.h>

int CalculateR2(int R1, int S)
{
    return 2 * S - R1;
}

void PrintResult(int R1, int S)
{
    int R2 = CalculateR2(R1, S);
    printf("%d\n", R2);
}

int main(void)
{
    int R1, S;
    scanf("%d %d", &R1, &S);
    PrintResult(R1, S);
}
