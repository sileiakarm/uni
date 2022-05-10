#include <stdio.h>

int main(void){
    int grades[100];
    int num1,num2,i,x;
    num1 = 0;
    num2 = 0;

    printf("Inserting the grades of the students...\n");
    
    for (i = 1; i < 101; i++) {

        printf("Enter a grade from 1 to 10:\n");
        scanf("%d", &x);

        while (x > 10 || x < 0) {
            printf("Input must be a number between 0 and 10, try again:\n");
            scanf("%d", &x);
        }
        grades[i] = x;
    }

    printf("Insertion of grades complete...\n");
    printf("Put the range of the grades you want to search [a,b]\n");
    scanf("%d,%d", &num1, &num2);

    while (num1 > num2) {
        printf("Number a must be smaller than b, try again:\n");
        scanf("%d %d", &num1, &num2);

    }

    printf("Searching for grades...\n");

    for (i = 1; i < 101; i++) {
        if (grades[i] >= num1 && grades[i]<= num2) {
            printf("student %d is in the range with a grade of %d\n",i,grades[i]);
        }

    }
    printf("Search done!\n");
}
