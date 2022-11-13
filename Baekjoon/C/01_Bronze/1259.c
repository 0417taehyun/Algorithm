// [ 백준 ] 1259번: 팰린드롬수

#include <stdio.h>
#include <string.h>

int is_break_loop(char number[6]) {
    if (strcmp(number, "0") == 0) {
        return 1;
    }
    return 0;
}

int is_palindrome_number(char number[6]) {
    int left = 0;
    int right = strlen(number) - 1;
    while (left < right) {
        if (number[left] != number[right]) {
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}

char* get_result_of_palindrome_validation(char number[6]) {
    if (is_palindrome_number(number) == 1) {
        return "yes";
    }
    return "no";
}

int main(void)
{
    while (1) {
        char number[6];
        scanf("%s", &number);
        
        if (is_break_loop(number)) {
            return 0;
        }
        printf("%s\n", get_result_of_palindrome_validation(number));
    }
}