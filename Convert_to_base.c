/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<string.h>
#include<math.h>
int main()
{
    char san[10];
    scanf("%s",san);
    int result =0;
    int j=0;
    for(int i = strlen(san)-1;i>=0;i--)
    {
        if(48<=san[i] && san[i]<=58)
        result = result+((san[i]-48)*pow(17,j));
        else
        {
            result =result+((san[i]-55)*pow(17,j));
        }
        j++;
    
        
      
    }
    printf("%d",result);
    

    return 0;
}
