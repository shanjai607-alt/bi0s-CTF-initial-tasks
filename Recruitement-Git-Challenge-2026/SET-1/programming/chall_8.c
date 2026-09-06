#include <stdio.h>

int main() {
    int n, i;
    int *p;
    long long fact = 1;

    scanf("%d", &n);

    p = &n;

    for (i = 1; i <= *p; i++) {
        fact = fact * i;
    }

    printf("Factorial:%lld", fact);

    return 0;
}