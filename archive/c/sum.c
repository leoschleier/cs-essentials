#include <stdio.h>

int sum(int a, int b);

int main(){
    int v;
    v = sum(3, 5);
    printf("Result: %d", v);

    return 0;
}

int sum(int a, int b){
    int c = a + b;
    return c;
}