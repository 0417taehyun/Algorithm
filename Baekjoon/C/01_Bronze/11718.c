// [ 백준 ] 11718번: 그대로 출력하기

#include <stdio.h>

int main(void)
{
    char str[101];
    
    // 버퍼에 남아 있는 값을 제거해야 해서 아래와 같이 앞에 띄어쓰기를 한 칸 써줘야 한다.
    while (scanf(" %[^\n]", &str) == 1) {
        printf("%s\n", str);
    }
}
