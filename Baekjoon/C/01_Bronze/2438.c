// [ 백준 ] 2438번: 별 찍기 - 1

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}