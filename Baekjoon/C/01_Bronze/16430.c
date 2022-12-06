// [ 백준 ] 16430번: 제리와 톰

#include <stdio.h>

void PrintLeftCheese(int A, int B)
{
    printf("%d %d\n", B - A, B);
}

int main(void)
{
    int A, B;
    scanf("%d %d", &A, &B);
    PrintLeftCheese(A, B);
}
