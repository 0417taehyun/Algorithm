// [ 백준 ] 1085번: 직사각형에서 탈출

#include <stdio.h>

int main(void)
{
    int x, y, w, h;
    scanf("%d %d %d %d", &x, &y, &w, &h);
    
    int min_x;
    if ((w - x) < x) {
        min_x = w - x;
    } else {
        min_x = x;
    }
    
    int min_y;
    if ((h - y) < y) {
        min_y = h - y;
    } else {
        min_y = y;
    }
    
    if (min_x < min_y) {
        printf("%d", min_x);
    } else {
        printf("%d", min_y);
    }
}