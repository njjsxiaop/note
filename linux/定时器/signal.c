#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/time.h>

void sigroutine()
{
    sleep(3);
    printf("SIGHUP!%d\n",time(NULL));
}

int main()
{
    int loop = 0;
    printf("process pid is %d.\n", getpid());

    signal(SIGHUP,sigroutine);

    while(loop < 10)
    {
        sleep(5);
        kill(getpid(),SIGHUP);
        loop++;
    }
    return 0;
}

