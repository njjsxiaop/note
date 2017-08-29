//折半查找（binary search）技术又称为二分查找。它的前提是线性表中的记录必须是关键码有序，线性表必须采用顺序存储。

#include <stdio.h>

#define ARRAY_NUM	6

int Binary_Search(int *a, int n, int key)
{
	int low,high,mid;
	low = 1;
	high = n;
	while(low<=high)
	{
		mid = (low + high) / 2;
		if(key < a[mid])
			high = mid - 1;
		else if(key > a[mid])
			low = mid + 1;
		else
			return mid;
	}
	
	return 0;
}

int main(int argc, char ** argv)
{
	int a[ARRAY_NUM];	
	int loop = 0;
	for(;loop < ARRAY_NUM; loop++)
	{
		scanf("%d", &a[loop]);
	}
	
	int result = Binary_Search(a, ARRAY_NUM ,atoi(argv[1]));
	printf("\nthe index of key is %d!\n",result);
	return 0;
}
