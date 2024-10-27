for dongu 3 child 
kend pros id ekran yazor 
fork poma olmycak cikack


/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include <unistad.t>
#include <
unistad.thissus types.h 

int main()
{
    int number = 0;
    pit_t pid = fork();
    
    if(pid ==0) {
        for (int i = 0; i <3 ;i++){
            number += 10;
            printf("Child process:number = %d  \n", number);
            sleep(1);
        } 
        exit(0);
        
    }else if(pid > 0 ){
        for (int i = 0 ; i < 3 ; i++){
            number -= 5;
            printf("Perint proces i:number  = %d  \n",number);
            sleep(1);
        }
        
        wait(null);
        printf("parent process : child tamamland . \n");
    } else {
        printf("fork basarisiz oldu \n");
 
    }
return 0;
}