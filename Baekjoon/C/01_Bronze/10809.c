// [ 백준 ] 10809번: 알파벳 찾기

#include <stdio.h>
#include <string.h>

int main(void)
{
    int diff = 'z' - 'a';
    int alphabet[diff + 1];
    for (int i = 0; i <= diff; i++) {
        alphabet[i] = -1;
    }

    char S[101];
    scanf("%s", &S);

    for (int j = 0; j < strlen(S); j++) {
        int index = S[j] - 'a';
        if (alphabet[index] == -1) {
            alphabet[index] = j;
        }
    }

    /*
    sizeof 함수의 경우 배열에 사용하면 배열 전체의 바이트 크기를 구한다.
    따라서 이 경우 26개의 정수형 요소가 들어 있기 때문에 4바이트씩 26개로 총 크기가 104가 된다.
    결과적으로 배열의 길이를 구하고 싶으면 배열의 첫 번째 요소의 바이트 크기로 전체 크기를 나누어야 한다.
    */
    int size = sizeof(alphabet) / sizeof(alphabet[0]);
    for (int k = 0; k < size; k++) {
        printf("%d ", alphabet[k]);
    }

}