// [ 백준 ] 10926번: ??!

#include <stdio.h>

char *DUPLICATE_MESSAGE = "\?\?!";

void PrintDuplicateUserIdMessage(char *user_id)
{
    printf("%s%s", user_id, DUPLICATE_MESSAGE);
}

int main(void)
{
    char user_id[51];
    scanf("%s", user_id);

}