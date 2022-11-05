// [ 백준 ] 2755번: 이번학기 평점은 몇점?

#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int total_credit = 0;
    double total_score = 0;
    for (int i = 0; i < N; i++) {
        char subject[101], score[3];
        int credit;
        scanf("%s %d %s", &subject, &credit, &score);

        if (strcmp(score, "A+") == 0) {
            total_score += (credit * 4.3);
        } else if (strcmp(score, "A0") == 0) {
            total_score += (credit * 4.0);
        } else if (strcmp(score, "A-") == 0) {
            total_score += (credit * 3.7);
        } else if (strcmp(score, "B+") == 0) {
            total_score += (credit * 3.3);
        } else if (strcmp(score, "B0") == 0) {
            total_score += (credit * 3.0);
        } else if (strcmp(score, "B-") == 0) {
            total_score += (credit * 2.7);
        } else if (strcmp(score, "C+") == 0) {
            total_score += (credit * 2.3);
        } else if (strcmp(score, "C0") == 0) {
            total_score += (credit * 2.0);
        } else if (strcmp(score, "C-") == 0) {
            total_score += (credit * 1.7);
        } else if (strcmp(score, "D+") == 0) {
            total_score += (credit * 1.3);
        } else if (strcmp(score, "D0") == 0) {
            total_score += (credit * 1.0);
        } else if (strcmp(score, "D-") == 0) {
            total_score += (credit * 0.7);
        }

        total_credit += credit;
    }

    printf("%.2lf", round((total_score / total_credit) * 100) / 100) ;
}
