// [ 백준 ] 20492번: 세금

#include <stdio.h>

double TAX_RATIO = 0.22;
double NEED_COST = 0.8;

int CalculateFirstCase(int cash)
{
    return cash - (cash * TAX_RATIO);
}

int CalculateSecondCase(int cash)
{
    return cash - ((cash - cash * NEED_COST) * TAX_RATIO);
}

void PrintResult(int cash)
{
    printf("%d %d\n", CalculateFirstCase(cash), CalculateSecondCase(cash));
}

int main(void)
{
    int N;
    scanf("%d", &N);
    PrintResult(N);
}
