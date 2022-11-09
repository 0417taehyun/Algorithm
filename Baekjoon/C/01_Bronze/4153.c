// [ 백준 ] 4153번: 직각삼각형

#include<stdio.h>

int main(void)
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    while (a !=0 && b != 0 && c != 0) {
        int x, y, z;
        if (a >= b && a >= c) {
            x = a;
            y = b;
            z = c;
        } else if (b >= a && b >= c) {
            x = b;
            y = a;
            z = c;
        } else {
            x = c;
            y = a;
            z = b;
        }
        
        if ((x * x) == ((y * y) + (z * z))) {
            printf("right\n");
        } else {
            printf("wrong\n");
        }
        scanf("%d %d %d", &a, &b, &c);
    }
}