// [ 백준 ] 1264번: 모음의 개수

#include <stdio.h>
#include <string.h>

char BREAK_POINT = '#';
char VOWELS[11] = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

int IsBreakPoint(char *sentence)
{
    if (strlen(sentence) == 1 && sentence[0] == BREAK_POINT) {
        return 1;
    }
    return 0;
}

int IsVowel(char letter)
{
    for (int i = 0; i < strlen(VOWELS); i++) {
        if (letter == VOWELS[i]) {
            return 1;
        }
    }
    return 0;
}

void PrintVowelsCount(char *sentence)
{
    int count = 0;
    for (int i = 0; i < strlen(sentence); i++) {
        if (IsVowel(sentence[i]) == 1) {
            count++;
        }
    }
    printf("%d\n", count);
}

int main(void)
{
    while (1) {
        char sentence[256];
        scanf(" %[^\n]", &sentence);
        if (IsBreakPoint(sentence) == 1) {
            break;
        }
        PrintVowelsCount(sentence);
    }
}