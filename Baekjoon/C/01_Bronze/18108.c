// [ 백준 ] 18108번: 1998년생인 내가 태국에서는 2541년생?!

#include <stdio.h>

int YEAR_GAP = 2541 - 1998;

void PrintConvertedYear(int year)
{
    printf("%d\n", year - YEAR_GAP);
}

int main(void)
{
    int year;
    scanf("%d", &year);
    PrintConvertedYear(year);
}
