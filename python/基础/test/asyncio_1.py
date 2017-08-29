#! /usr/bin/env python
# -*- coding: utf-8 -*-

from time import ctime
import asyncio

@asyncio.coroutine

def hello():
    print('Hello World! %s' % ctime())
    r = yield from asyncio.sleep(10)
    print("Hello Again! %s" % ctime())

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()

if __name__ == '__main__':
    main()
