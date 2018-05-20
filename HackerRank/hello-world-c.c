#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*

URL: https://www.hackerrank.com/challenges/hello-world-c/problem

Summary:  Add a print statement to print "Hello, World!" followed by the
scanf() input on a new line.

*/

int main() 
{
	
    char s[100];
    scanf("%[^\n]%*c", &s);
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("Hello, World!\n%s", s);
    return 0;
}
