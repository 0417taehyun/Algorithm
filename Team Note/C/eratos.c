/*
    소수 판별 방법 에라토스테네스의 체 알고리즘
    시간 복잡도: O(Nlog(logN)) (선형 시간인 O(N) 근사)
    공간 복잡도: O(N)

    제곱근의 경우 math 헤더에서 제공하는 sqrt 함수 사용이 불가할 때 아래와 같이 두 가지 방법 사용 가능
    1. 바빌로니아 법
    2. 뉴턴 방법
*/

#include <stdio.h>
#include <math.h>

void InitializeNumbers(int numbers[], int N)
{
    numbers[0] = 0;
    numbers[1] = 0;
    for (int i = 2; i <= N; i++) {
        numbers[i] = 1;
    }
}

void Eratos(int numbers[], int N)
{
    for (int i = 2; i <= sqrt(N); i++) {
        if (numbers[i] == 0) {
            continue;
        }
        for (int j = i + i; j <= N; j += i) {
            numbers[j] = 0;
        }
    }
}

void PrintPrimeNumbersInArray(int numbers[], int start, int end)
{
    for (int number = start; number <= end; number++) {
        if (numbers[number] == 1) {
            printf("%d\n", number);
        }
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    int numbers[N+1];
    InitializeNumbers(numbers, N);
    Eratos(numbers, N);
    PrintPrimeNumbersInArray(numbers, 2, N);
}
