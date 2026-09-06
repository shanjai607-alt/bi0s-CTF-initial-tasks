#include <stdio.h>

int main() {
    char str[100];
    int i, v = 0, c = 0;

    scanf("%[^\n]", str);

    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' ||
            str[i] == 'o' || str[i] == 'u') {
            v++;
        }
        else if (str[i] >= 'a' && str[i] <= 'z') {
            c++;
        }
    }

    printf("Vowels: %d\n", v);
    printf("Consonants: %d", c);

    return 0;
}