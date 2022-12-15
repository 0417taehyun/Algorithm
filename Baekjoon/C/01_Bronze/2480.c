// [ 백준 ] 2480번: 주사위 세 개

#include <stdio.h>

enum Dice { ONE = 1, TWO, THREE };

int ONE_DICE_SAME_MULTIPLY = 100;
int TWO_DICES_SAME_MULTIPLY = 100;
int TWO_DICES_SAME_PRIZE = 1000;
int THREE_DICES_SAME_MULTIPLY = 1000;
int THREE_DICES_SAME_PRIZE = 10000;

int GetSameDice(int first, int second, int third)
{
    if (first == second) {
        return first;
    }
    if (second == third) {
        return second;
    }
    return third;
}

int GetMaximumDice(int first, int second, int third)
{
    if (first >= second && first >= third) {
        return first;
    }
    if (second >= first && second >= third) {
        return second;
    }
    return third;
}

int GetSameDiceCount(int first, int second, int third)
{
    if (first == second && first == third) {
        return THREE;
    }
    if (first != second && first != third && second != third) {
        return ONE;
    }
    return TWO;
}

int GetWinningPrize(int first, int second, int third)
{
    int base_prize = 0;
    int adder = 0;
    int count = GetSameDiceCount(first, second, third);
    if (count == ONE) {
        adder = GetMaximumDice(first, second, third) * ONE_DICE_SAME_MULTIPLY;
        return base_prize + adder;
    }
    if (count == TWO) {
        base_prize = TWO_DICES_SAME_PRIZE;
        adder = GetSameDice(first, second, third) * TWO_DICES_SAME_MULTIPLY;
        return base_prize + adder;
    }
    base_prize = THREE_DICES_SAME_PRIZE;
    adder = GetSameDice(first, second, third) * THREE_DICES_SAME_MULTIPLY;
    return base_prize + adder;
}

void PrintWinningPrize(int first, int second, int third)
{
    int prize = GetWinningPrize(first, second, third);
    printf("%d\n", prize);
}

int main(void)
{
    int first, second, third;
    scanf("%d %d %d", &first, &second, &third);
    PrintWinningPrize(first, second, third);
}
