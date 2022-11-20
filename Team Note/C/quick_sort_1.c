/*
    배열의 첫 번째 요소를 피봇(Pivot)의 기준으로 한 일반 퀵 정렬
    시간 복잡도: O(NlogN)
    공간 복잡도: O(N)

    최악의 상황 -이미 정렬된 배열이 주어지는 경우- 에서 시간 복잡도는 O(N^2)이기 때문에 최적화를 위해 아래와 같이 두 가지 방법 사용 가능
    1. 피봇의 기준을 배열의 첫 번째 요소가 아닌 중앙값으로 하는 방법
    2. 주어진 배열을 무작위로 섞는 방법이 있다.
*/

#include <stdio.h>

void InitializeArray(int numbers[], int N)
{
    for (int i = 0; i < N; i++) {
        scanf("%d", &numbers[i]);
    }
}

void Swap(int *left, int *right)
{
    int temp = *left;
    *left = *right;
    *right = temp;
}

int DividePartition(int numbers[], int left, int right)
{
    int first = left;
    int pivot = numbers[first];
    left++;
    while (left <= right) {
        while (left < right && numbers[left] < pivot) {
            left++;
        }
        while (left <= right && numbers[right] >= pivot) {
            right--;
        }
        if (left >= right) {
            break;
        }
        Swap(&numbers[left], &numbers[right]);
    }
    Swap(&numbers[first], &numbers[right]);
    return right;
}

void QuickSort(int numbers[], int left, int right)
{
    if (left < right) {
        int pivot = DividePartition(numbers, left, right);
        QuickSort(numbers, left, pivot - 1);
        QuickSort(numbers, pivot + 1, right);
    }
}

void PrintSortedArray(int numbers[], int N)
{
    for (int i = 0; i < N; i++) {
        printf("%d ", numbers[i]);
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    int numbers[N];
    InitializeArray(numbers, N);
    QuickSort(numbers, 0, N-1);
    PrintSortedArray(numbers, N);
}
