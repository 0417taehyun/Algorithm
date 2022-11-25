// [ 백준 ] 4999번: 아!

#include <stdio.h>
#include <string.h>

char* GetComparisonResult(char* input, char* target)
{
    if (strlen(input) >= strlen(target)) {
        return "go";
    }
    return "no";
}

int main(void)
{
    char user[1001], doctor[1001];
    scanf("%s %s", &user, &doctor);
    printf("%s", GetComparisonResult(user, doctor));
}