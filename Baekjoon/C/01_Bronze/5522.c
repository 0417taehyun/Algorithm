// [ 백준 ] 5522번: 카드 게임

#include <stdio.h>

int GetTotalPoint()
{
    int total = 0;
    int point;
    while (scanf("%d", &point) == 1) {
        total = total + point;
    }
    return total;
}

void PrintResult()
{
    int result = GetTotalPoint();
    printf("%d\n", result);
}

int main(void)
{
    PrintResult();
}
