//数组里面只有0和1，且顺序从小到大排列。求出第一个1的索引。

#include <stdio.h>

#define ARRAY_NUM	6


int binary_search(int * a, int n)
{
	int low = 1;
	int high = n;
	
	while(low <= high)
	{
		int mid = (low + high) / 2;
		if(0 == a[mid])
			low = mid + 1;
		else if(1 == a[mid] && a[mid - 1] != 0)
			high = mid - 1;
		else
			return mid;
	}	

	printf("\nThere is no %d in the array!", 1);
	return 0;
}


int main(int argc, char ** argv)
{
	int loop = 0;
	int a[6];

	printf("import your arrry, please!");
	scanf("%d,%d,%d,%d,%d,%d", &a[0], &a[1], &a[2], &a[3], &a[4], &a[5]);

	int result = binary_search(a, ARRAY_NUM);
	printf("\nThe first index of 1 is %d!\n", result);

	return 0;
}
