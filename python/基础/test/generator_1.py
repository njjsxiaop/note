#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

def main():
    count = int(sys.argv[1])
    g = fib(count)

    while True:
        try:
            x = next(g)
            print("g:%d" % x)
        except StopIteration as e:
            print("Generator return value:%s" % e.value)
            break


if __name__ == '__main__':
    main()
