#include<stdio.h>
#include<string.h>

int main()
{
  int len=0;
  int count =1;
  char a[100];
  fgets(a,100,stdin);
  len = strlen(a);
  if(len!=0){
    for(int i=0;i<len;i++){
      if(a[i]==' '){
        count +=1;
      }
      if(a[i]!=' '){
        printf("%c",a[i]);
        }
      else{
        printf("\n");
      }
    }
  }
  printf("\n\nThe Total number of words: %d",count);
  return 0;
}