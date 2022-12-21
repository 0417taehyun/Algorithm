// [ 백준 ] 15727번: 조별과제를 하려는데 조장이 사라졌다

#include <stdio.h>

int MAXIMUM_MOVE_LENGTH = 5;
enum Move { ZERO, ONE };

int CalculateMaximumMoveTimes(int L)
{
    return (int) L / MAXIMUM_MOVE_LENGTH;
}

int CalculateRemainedMoveTimes(int L)
{
    int remainder = L % MAXIMUM_MOVE_LENGTH;
    if (remainder > 0) {
        return ONE;
    }
    return ZERO;
}

void PrintTotalMoveTimes(int L)
{
    int maximum_move_times = CalculateMaximumMoveTimes(L);
    int rest_of_move_times = CalculateRemainedMoveTimes(L);
    printf("%d\n", maximum_move_times + rest_of_move_times);
}

int main(void)
{
    int L;
    scanf("%d", &L);
    PrintTotalMoveTimes(L);
}
