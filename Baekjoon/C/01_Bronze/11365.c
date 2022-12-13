// [ 백준 ] 11365번: !밀비 급일

#include <stdio.h>
#include <string.h>

char BREAK_POINT[4] = "END";
char NEW_LINE = '\n';

int IsBreakPoint(char *sentence)
{
    if (strcmp(sentence, BREAK_POINT) == 0) {
        return 1;
    }
    return 0;
}

void PrintNewLine()
{
    printf("%c", NEW_LINE);
}

void PrintSecretMessage(char *sentence)
{
    for (int i = strlen(sentence) - 1; i >= 0; i--) {
        printf("%c", sentence[i]);
    }
    PrintNewLine();
}

int main(void)
{
    while (1) {
        char sentence[501];
        scanf(" %[^\n]", &sentence);
        if (IsBreakPoint(sentence) == 1) {
            break;
        }
        PrintSecretMessage(sentence);
    }
}
