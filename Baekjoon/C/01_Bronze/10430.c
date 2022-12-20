// [ 백준 ] 10430번: 나머지

#include <stdio.h>

void PrintAddMod(int A, int B, int C)
{
    printf("%d\n", (A + B) % C);
}

void PrintDistributedAddMod(int A, int B, int C)
{
    printf("%d\n", ((A % C) + (B % C)) % C);
}

void PrintProductMod(int A, int B, int C)
{
    printf("%d\n", (A * B) % C);
}

void PrintDistributedProductMod(int A, int B, int C)
{
    printf("%d\n", ((A % C) * (B % C)) % C);
}

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    PrintAddMod(A, B, C);
    PrintDistributedAddMod(A, B, C);
    PrintProductMod(A, B, C);
    PrintDistributedProductMod(A, B, C);
}