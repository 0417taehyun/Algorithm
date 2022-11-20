// [ 백준 ] 1929번: 소수 구하기

#include <stdio.h>
#include <math.h>

void PrintPrimeNumbersInArray(int numbers[], int start, int end)
{
    for (int number = start; number <= end; number++) {
        if (numbers[number] == 1) {
            printf("%d\n", number);
        }
    }
}

void Eratos(int numbers[], int N)
{
    numbers[1] = 0;
    for (int i = 2; i <= sqrt(N); i++) {
        if (numbers[i] == 0) {
            continue;
        }
        for (int j = i + i; j <= N; j += i) {
            numbers[j] = 0;
        }
    }
}

int main(void)
{
    int M, N;
    scanf("%d %d", &M, &N);
    int numbers[N+1];
    for (int i = 1; i <= N; i++) {
        numbers[i] = 1;
    }
    Eratos(numbers, N);
    PrintPrimeNumbersInArray(numbers, M, N);
}
