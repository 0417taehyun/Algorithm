// [ 백준 ] 16170번: 오늘의 날짜는?

#include <stdio.h>
#include <time.h>

int YEAR_ADDER = 1900;
int MONTH_ADDER = 1;

int GetYear(struct tm *tm)
{
    return tm -> tm_year + YEAR_ADDER;
}

int GetMonth(struct tm *tm)
{
    return tm -> tm_mon + 1;
}

int GetDay(struct tm *tm)
{
    return tm -> tm_mday;
}

void PrintCurrentDate()
{
    time_t now = time(NULL);
    struct tm *tm = gmtime(&now);
    printf("%d\n%d\n%d\n", GetYear(tm), GetMonth(tm), GetDay(tm));
}

int main(void)
{
    PrintCurrentDate();
    return 0;
}