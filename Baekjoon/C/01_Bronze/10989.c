// [ 백준 ] 10989번: 수 정렬하기 3

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    int numbers[10001] = {0, };
    for (int i = 0; i < N; i++) {
        int number;
        scanf("%d", &number);
        numbers[number]++;
    }
    for (int i = 1; i < 10001; i++) {
        while (numbers[i] > 0) {
            printf("%d\n", i);
            numbers[i]--;
        }
    }
}