// [ 백준 ] 16394번: 홍익대학교

#include <stdio.h>

int SCHOOL_ANNIVERSARY_YEAR = 1946;

void PrintYearGap(int year)
{
    printf("%d\n", year - SCHOOL_ANNIVERSARY_YEAR);
}

int main(void)
{
    int year;
    scanf("%d", &year);
    PrintYearGap(year);
}