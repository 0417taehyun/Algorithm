// [ 백준 ] 2754번: 학점계산

#include <stdio.h>

int main(void)
{
    char score[3];
    scanf("%s", &score);

    if (score[0] == 'A') {
        if (score[1] == '+') {
            printf("4.3");
        } else if (score[1] == '0') {
            printf("4.0");
        } else {
            printf("3.7");
        }

    } else if (score[0] == 'B') {
        if (score[1] == '+') {
            printf("3.3");
        } else if (score[1] == '0') {
            printf("3.0");
        } else {
            printf("2.7");
        }

    } else if (score[0] == 'C') {
        if (score[1] == '+') {
            printf("2.3");
        } else if (score[1] == '0') {
            printf("2.0");
        } else {
            printf("1.7");
        }

    } else if (score[0] == 'D') {
        if (score[1] == '+') {
            printf("1.3");
        } else if (score[1] == '0') {
            printf("1.0");
        } else {
            printf("0.7");
        }

    } else {
        printf("0.0");
    }
}