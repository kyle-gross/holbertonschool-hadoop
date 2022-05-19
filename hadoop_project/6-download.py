#!/usr/bin/env python3
"""This module contains the function download()"""

from snakebite.client import Client


def download(l):
    """Retrieves from hdfs the files listed in l and stores them in the /tmp
    directory of the user
    """
    client = Client('127.0.1.1', 9000)

    for x in client.copyToLocal(l, '/tmp'):
        print(x)


if __name__ == '__main__':
    l = ["/holbies/input/lao.txt"]
    download(l)
    lao =  open("/tmp/lao.txt", "r")
    print(lao.read())
    lao.close()