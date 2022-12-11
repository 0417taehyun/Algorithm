// [ 백준 ] 2440번: 별 찍기 - 3

#include <stdio.h>

char STAR = '*';
char NEW_LINE = '\n';

void PrintNewLine()
{
    printf("%c", NEW_LINE);
}

void PrintStars(int times)
{
    for (int i = 0; i < times; i++) {
        printf("%c", STAR);
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    for (int i = N; i > 0; i--) {
        PrintStars(i);
        PrintNewLine();
    }
}