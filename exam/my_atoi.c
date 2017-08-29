#include <stdio.h>
#include <stdbool.h>

#define INT_MAX 0x7fffffff

int main(int argc, char *argv[])
{
    printf("value is :%d\n.", my_atoi(argv[1]));
    return 0;
}

int my_atoi(char *str)
{
    bool is_minus = false;
    long result = 0;

    if(NULL == str)
    {
        printf("null point error!\n");
        return 0;
    }

    while(0 != *str)
    {
        if((*str > '9' || *str < '0') && *str != '+' && *str != '-')
        {
            str++;
            continue;
        }
        break;
    }

    if(0 == *str)
    {
        printf("origin str error!\n");
        return 0;
    }

    if(*str == '-')
    {
        is_minus = true;
        str++;
    }

    if(*str == '+')
    {
        str++;
    }

    if(0 == *str)
    {
        printf("origin str error!\n");
        return 0;
    }

    while(0 != *str && *str >= '0' && *str <= '9')
    {
        result = result * 10 + *str - '0';
        str++;
    }


    if((!is_minus && result > INT_MAX) || (is_minus && result > (long)INT_MAX + 1))
    {
        printf("value overflow!\n");
    }

    if(is_minus)
        return 0 - result;

    return result;
}

