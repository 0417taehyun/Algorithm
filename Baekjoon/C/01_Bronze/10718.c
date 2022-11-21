// [ 백준 ] 10718번: We love kriii

#include <stdio.h>

char* MESSAGE = "강한친구 대한육군";

void PrintMessage(int times)
{
    for (int i = 0; i < times; i++) {
        printf("%s\n", MESSAGE);
    }
}

int main(void)
{
    PrintMessage(2);
}