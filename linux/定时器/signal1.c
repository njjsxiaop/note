#include <stdio.h>
#include <signal.h>
#include <sys/time.h>

int main()
{
    sigset_t block;
    struct itimerval itv;

    sigemptyset(&block);
    sigaddset(&block, SIGALRM);
    sigprocmask(SIG_BLOCK, &block, NULL);

    itv.it_interval.tv_sec = 5;
    itv.it_interval.tv_usec = 0;
    itv.it_value = itv.it_interval;
    setitimer(ITIMER_REAL, &itv, NULL);

    while(1)
    {
        sleep(2);
        printf("%d\n",time(NULL));
        sigwaitinfo(&block, NULL);
    }

    return 0;
}
