#include <stdlib.h>
#include <stdio.h>

int main()
{
    char *value = getenv("HOSTNAME");
    printf("%s\n",value);
    return 0;
}
