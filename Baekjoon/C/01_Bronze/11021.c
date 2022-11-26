// 11021번: A+B - 7

#include <stdio.h>

char *MESSAGE = "Case #";
char SEPARATOR = ':';

int SumTwoNumbers(int A, int B)
{
    return A + B;
}

void PrintSumResult(int index, int sum)
{
    printf("%s%d%c %d\n", MESSAGE, index, SEPARATOR, sum);
}

void PrintAllSumResult(int range)
{
    for (int index = 1; index <= range; index++) {
        int A, B;
        scanf("%d %d", &A, &B);
        PrintSumResult(index, SumTwoNumbers(A, B));
    }
}

int main(void)
{
    int T;
    scanf("%d", &T);
    PrintAllSumResult(T);
}