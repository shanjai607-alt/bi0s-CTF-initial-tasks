#include <stdio.h>

int main() {
    int n, i, x, min, max;

    scanf("%d", &n);

    scanf("%d", &x);
    min = x;
    max = x;

    for (i = 1; i < n; i++) {
        scanf("%d", &x);

        if (x < min)
            min = x;

        if (x > max)
            max = x;
    }

    printf("Minimum: %d\n", min);
    printf("Maximum: %d", max);

    return 0;
}