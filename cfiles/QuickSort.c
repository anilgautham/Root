#include<stdio.h>
#include<stdlib.h>
void swap(int* x,int* y){
  int temp= *x;
  *x=*y;
  *y=temp;
}
int partition(int arr[],int low, int high){
  int pivot =arr[high];
  int i=low-1;
  for(int j=low;j<=high-1;j++){
    if(arr[j]<=pivot){
      i++;
      swap(&arr[i],&arr[j]);
    }
  }
  swap(&arr[i+1],&arr[high]);
  return (i+1);
}
void quickSort(int arr[],int low,int high){
  if(low<high){
    int part = partition(arr,low,high);
    quickSort(arr,low,part-1);
    quickSort(arr,part+1,high);
  }
}
void printArray(int arr[],int q){
  for(int i=0;i<q;i++){
    printf("%d ",arr[i]);
  }
}
int main(){
  int *arr,q;
  printf("Enter the size of your array:\n");
  scanf("%d",&q);
  arr = (int*)malloc(sizeof(int)*q);
  printf("Enter the array elements:\n");
  for(int i=0;i<q;i++)
  scanf("%d",&arr[i]);
  printf("\nYour Array is:\n");
  printArray(arr,q);
  quickSort(arr,0,q-1);
  printf("\nThe sorted array is:\n");
  printArray(arr,q);
  printf("\n");
  free(arr);
  return 0;
}
