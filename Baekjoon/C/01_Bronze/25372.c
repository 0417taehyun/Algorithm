// [ 백준 ] 25372번: 성택이의 은밀한 비밀번호

#include <stdio.h>
#include <string.h>

char *GetResult(char *password)
{
    if (strlen(password) >= 6 && strlen(password) <= 9) {
        return "yes";
    }
    return "no";
}

void PrintResult(int N)
{
    for (int i = 0; i < N; i++) {
        char password[21];
        scanf("%s", &password);
        printf("%s\n", GetResult(password));
    }
}

int main(void)
{
    int N;
    scanf("%d", &N);
    PrintResult(N);
}
