// [ 백준 ] 2386번: 도비의 영어 공부

#include <stdio.h>
#include <string.h>

char BREAK_FLAG = '#';
int MAX_SIZE = 250;
int ASCII_DIFFERENCE = 'a' - 'A';

int IsSameAlphabet(char lower, int target)
{
    char upper = lower - ASCII_DIFFERENCE;
    if (upper == target || lower == target ) {
        return 1;
    }
    return 0;
}

int CountTargetAlphabet(char alphabet, char *sentence)
{
    int count = 0;
    for (int i = 0; i < strlen(sentence); i++) {
        if (IsSameAlphabet(alphabet, sentence[i]) == 1) {
            count++;
        }
    }
    return count;
}

int main(void)
{
    while (1) {
        char target;
        scanf(" %c", &target);
        if (target == BREAK_FLAG) {
            break;
        }
        char sentence[MAX_SIZE+1];
        scanf("%[^\n]", &sentence);
        printf("%c %d\n", target, CountTargetAlphabet(target, sentence));
    }
}
