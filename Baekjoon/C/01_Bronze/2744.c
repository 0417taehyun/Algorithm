// [ 백준 ] 2744번: 대소문자 바꾸기

#include <stdio.h>
#include <string.h>
#include <ctype.h> // 대소문자 변경 메서드 사용을 위한 라이브러리

int main(void)
{
    int lower_a = 'a';
    int upper_a = 'A';
    int diff = lower_a - upper_a;

    char str[101];
    scanf("%s", &str);

    for (int i = 0; i < strlen(str); i++) {
        int reversed;

        if ((int) str[i] >= lower_a){
            reversed = (int) str[i] - diff;
        } else {
            reversed = (int) str[i] + diff;
        }

        printf("%c", (char) reversed);
    }

    
    /*
    아래와 같이 string 헤더에 들어 있는 메서드를 사용해서 더 간단하게 풀 수도 있다는 걸 찾았는데
    strupr 및 strlwr 메서드는 내장 메서드가 아니기 때문에 기본적으로 제공하는 라이브러리에 포함되어 있지 않을 수 있다는 질의응답을 보았다.
    */
    for (int i = 0; i < strlen(str); i++) {
        if ((int) str[i] >= 'a') {
            printf("%c", strupr(str[i]));
        } else {
            printf("%c", strlwr(str[i]));
        }
    }


    /*
    아래와 같이 ctype 헤더에 들어 있는 메서드를 사용하면 정상적으로 대소문자 변경이 가능하다.
    */
    for (int i = 0; i < strlen(str); i++) {
        if ((int) str[i] >= 'a') {
            printf("%c", toupper(str[i]));
        } else {
            printf("%c", tolower(str[i]));
        }
    }
}