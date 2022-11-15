// [ 백준 ] 1978번: 소수 찾기 

#include <stdio.h>

int IsPrimeNumber(int number)
{
    if (number == 1) {
        return 0;
    }
    for (int i = 2; i < number; i++) {
        if (number % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(void)
{
    int answer = 0;

    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int number;
        scanf("%d", &number);
        if (IsPrimeNumber(number) == 1) {
            answer++;
        }
    }
    printf("%d", answer);
}