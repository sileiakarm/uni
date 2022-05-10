#include <stdio.h>

void MoveRight(int *cities,int startIndex)
{
    int j,temp;
    j=99;
    for(int i=startIndex;i<100;i++)
    {
            temp = cities[j];
            cities[j]=cities[i];
            cities[i]=temp;
    }
}

int main(void){
    int cities[100];
    int chk,i,j,temp,first,second,temp2,x;

    printf("Initalizing...\n");


    for (i = 1; i<=100; i++) {
        printf("Enter a number for the population:\n");
        scanf("%d", &x);

         while (x < 0) {
            printf("You can't have a negative number for population!\n");
            printf(" The number has to be equal or greater than zero, try again:\n");
            scanf("%d", &x);
        }
        
        for(j=0;j<=i;j++)
        {
            if(x<cities[j])
            {
                MoveRight(cities,j);
                cities[j]=x;
                break;
            }
        }

    }

    printf("Initializion done...\n");
    printf("Printing results...\n");

    for (i = 1; i < 100; i++) {
        printf("%d\n",cities[i]);
    }

    printf("Done!\n");
}
