// [ 백준 ] 4101번: 크냐?

#include <stdio.h>

char* BIGGER_TRUE = "Yes";
char* BIGGER_FALSE = "No";

int IsBreakFlag(int first_number, int second_number)
{
    if (first_number == 0 && second_number == 0) {
        return 1;
    }
    return 0;
}

char* GetCompareResult(int first_number, int second_number)
{
    if (first_number > second_number) {
        return BIGGER_TRUE;
    }
    return BIGGER_FALSE;
}

int main(void)
{
    while (1) {
        int first_number, second_number;
        scanf("%d %d", &first_number, &second_number);
        if (IsBreakFlag(first_number, second_number) == 1) {
            break;
        }
        printf("%s\n", GetCompareResult(first_number, second_number));
    }
}