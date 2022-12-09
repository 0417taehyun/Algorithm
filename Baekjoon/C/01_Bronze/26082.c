// [ 백준 ] 26082번: WARBOY

#include <stdio.h>

int DIFFERENCE = 3;

int CalculatePricePerPerformance(int price, int performance)
{
    return performance / price;
}

void PrintWarboyPerformance(int price_per_performance, int price)
{
    int performance = price_per_performance * price;
    printf("%d\n", performance);
}

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    int competitor = CalculatePricePerPerformance(A, B);
    int warboy_price_per_performance = competitor * DIFFERENCE;
    PrintWarboyPerformance(warboy_price_per_performance, C);
}