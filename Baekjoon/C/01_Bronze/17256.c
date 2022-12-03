// [ 백준 ] 17256번: 달달함이 넘쳐흘러

#include <stdio.h>

typedef struct
{
    int x;
    int y;
    int z;
} Cake;

Cake CreateCake()
{
    Cake cake;
    scanf("%d %d %d", &(cake.x), &(cake.y), &(cake.z));
    return cake;
}

Cake CalculateCake(Cake a, Cake c)
{
    Cake b;
    b.x = c.x - a.z;
    b.y = c.y / a.y;
    b.z = c.z - a.x;
    return b;
}

void PrintCakeNumbers(Cake cake)
{
    printf("%d %d %d\n", cake.x, cake.y, cake.z);
}

int main(void)
{
    Cake a = CreateCake();
    Cake c = CreateCake();
    Cake b = CalculateCake(a, c);
    PrintCakeNumbers(b);
}