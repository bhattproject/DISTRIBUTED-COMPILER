/*Program code-To sort the numbers 
of array
Name:RAJEEV BHATT
	Section:A
	Roll No:2261459
	Branch:CSE  
*/
#include <stdio.h>
#include<stdlib.h>
void sort(int,int *);
int main(){
int n,*p,i;
printf("Enter range:");
scanf("%d",&n);
p=(int *) malloc(n*sizeof(int));
for(i=0;i<=n-1;i++){
 scanf("%d",p+i);
}
sort(n,p);
printf("sorted elements:");
for(i=0;i<=n-1;i++){
printf("%d\t",*(p+i));


} }

void sort(int n,int *p)
{
 	int i,j,temp;
 	for (i=0;i<=n-1;i++){
 		for(j=0;j<=n-2-i;j++){
 		   if(*(p+j)>*(p+j+1)){
 		   	 temp=*(p+j);
 		   	 *(p+j)=*(p+j+1);
 		   	 *(p+j+1)=temp;
			}	
		 }
	 }
}
/*OUTPUT:
Enter range:3
21
34
222

sorted elements:21      34      222
*/
