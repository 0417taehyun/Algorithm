// [ 백준 ] 10808번: 알파벳 개수

#include <stdio.h>
#include <string.h>

int ASCII_LOWER_A = 'a' - 0;

int GetAlphabetIndex(char letter)
{
    return letter - ASCII_LOWER_A;
}

int *CreateAlphabet()
{
    int *alphabet = malloc(sizeof(int) * 26);
    for (int i = 0; i < 26; i++) {
        alphabet[i] = 0;
    }
    return alphabet;
}

int *CountAlphabet(char *word)
{
    int *alphabet = CreateAlphabet();
    for (int i = 0; i < strlen(word); i++) {
        int index = GetAlphabetIndex(word[i]);
        alphabet[index]++;
    }
    return alphabet;
}

void PrintAlphabetCount(char *word)
{
    int *alphabet = CountAlphabet(word);
    for (int i = 0; i < 26; i++) {
        printf("%d ", *(alphabet + i));
    }
}

int main(void)
{
    char S[101];
    scanf("%s", &S);
    PrintAlphabetCount(S);
}