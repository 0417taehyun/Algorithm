// [ 백준 ] 2475번: 검증수

#include <stdio.h>
#include <string.h>

int main(void)
{
    char numbers[10];
    scanf("%[^\n]", &numbers);
    numbers[strlen(numbers) - 1] = '\0';

    int sum = 0;
    for (int i = 0; i < strlen(numbers); i++) {
        if (numbers[i] != ' ') {
            int curr = numbers[i] - '0';
            sum += (curr * curr);
        }
    }

    printf("%d", sum % 10);
}