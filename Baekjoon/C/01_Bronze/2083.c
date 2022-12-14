// [ 백준 ] 2083번: 럭비 클럽

#include <stdio.h>
#include <string.h>

char *BREAK_POINT_NAME = "#";
int BREAK_POINT_AGE = 0;
int BREAK_POINT_WEIGHT = 0;
int SENIOR_AGE = 17;
int SENIOR_WEIGHT = 80;
char *SENIOR = "Senior";
char *JUNIOR = "Junior";

typedef struct
{
    int age;
    int weight;
    char name[11];
} Member;

int IsBreakPoint(char *name, int age, int weight)
{
    if (
        strcmp(name, BREAK_POINT_NAME) == 0
        &&
        age == BREAK_POINT_AGE
        &&
        weight == BREAK_POINT_WEIGHT
    ) {
        return 1;
    }
    return 0;
}

Member *CreateMember(char *name, int age, int weight)
{
    Member *member = malloc(sizeof(member));
    strcpy(member -> name, name);
    member -> age = age;
    member -> weight = weight;
    return member;
}

char *GetMemberType(Member *member)
{
    if (
        member -> age > SENIOR_AGE
        ||
        member -> weight >= SENIOR_WEIGHT
    ) {
        return SENIOR;
    }
    return JUNIOR;
}

void PrintMemberType(Member *member)
{
    char *type = GetMemberType(member);
    printf("%s %s\n", member -> name, type);
    free(member);
}

int main(void)
{
    while (1) {
        char name[11];
        int age, weight;
        scanf("%s %d %d", &name, &age, &weight);
        if (IsBreakPoint(name, age, weight) == 1) {
            break;
        }
        Member *member = CreateMember(name, age, weight);
        PrintMemberType(member);
    }
}
