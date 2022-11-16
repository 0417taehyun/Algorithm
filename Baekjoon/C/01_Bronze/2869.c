// [ 백준 ] 2869번: 달팽이는 올라가고 싶다

#include <stdio.h>
#include <math.h>

int main(void)
{
    int A, B, V;
    scanf("%d %d %d", &A, &B, &V);
    printf("%d", (int) ceil((double) (V-A)/(A-B)) + 1);
}
