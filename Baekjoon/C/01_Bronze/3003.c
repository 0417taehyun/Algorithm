// [ 백준 ] 3003번: 킹, 퀸, 룩, 비숍, 나이트, 폰

#include <stdio.h>

enum Chess { KING=1, QUEEN=1, ROOK=2, BISHOP=2, KNIGHT=2, PAWN=8 };

int main(void)
{
    int king, queen, rook, bishop, knight, pawn;
    scanf("%d %d %d %d %d %d", &king, &queen, &rook, &bishop, &knight, &pawn);
    printf(
        "%d %d %d %d %d %d\n",
        KING-king, QUEEN-queen, ROOK-rook,
        BISHOP-bishop, KNIGHT-knight, PAWN-pawn
    );
}