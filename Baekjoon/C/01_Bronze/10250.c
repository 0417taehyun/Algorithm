// [ 백준 ] 10250번: ACM 호텔

#include <stdio.h>

int main(void)
{
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int H, W, N;
        scanf("%d %d %d", &H, &W, &N);

        int X = (int) N / H;
        int Y = N % H;
        if (Y == 0) {
            Y = H;
        } else {
            X++;
        }
        int room_number = Y * 100 + X;
        printf("%d\n", room_number);
    }
}