#!/usr/bin/env python3.6

from myThread import MyThread
from time import ctime, sleep

def fib(x):
    #sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    #sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))

def sum1(x):
    #sleep(0.1)
    if x < 2:
        return 1
    return (x + sum1(x-1))

funcs = [fib, fac, sum1]
n = 35

def main():
    nfuncs = range(len(funcs))

    print("*****SINGLE THREAD*****")
    for i in nfuncs:
        print("starting %s at:%s" % (funcs[i].__name__, ctime()))
        print("%d" % (funcs[i](n)))
        print("%s finished at:%s" % (funcs[i].__name__, ctime()))


    print("*****MULTIPLE THREADS*****")
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print("%d" % (threads[i].getResult()))

    print("all DONE!")

if __name__ == '__main__':
    main()



