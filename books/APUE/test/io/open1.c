#include <fcntl.h>
#include <stdio.h>
int main()
{
//int ret = open("/home/xiaopeng/python/1", O_RDONLY);
  //  int ret1 = open("/home/xiaopeng/python/1", O_RDONLY | O_EXCL);
    //int ret2 = open("/home/xiaopeng/python/1", O_RDONLY | O_EXCL | O_CREAT);
    //printf("ret = %d\tret1 = %d\tret2 = %d\n",ret, ret1, ret2);

    //ret = open("/home/xiaopeng/python/2", O_RDONLY);
    //ret1 = open("/home/xiaopeng/python/2", O_RDONLY | O_EXCL);
    /*ret2 =*/ open("/home/xiaopeng/python/2", O_RDONLY | O_EXCL | O_CREAT);
    //printf("ret = %d\tret1 = %d\tret2 = %d\n",ret, ret1, ret2);
    return 0;
}
