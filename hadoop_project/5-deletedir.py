#!/usr/bin/env python3
"""This module contains the function deletedir()"""

from snakebite.client import Client


def deletedir(l):
    """Deletes the directory `l` from hdfs"""
    client = Client('127.0.1.1', 9000)

    l.reverse()
    # We could alternatively NOT have to reverse the list, by using the
    # snakebite client method: client.delete(<path>, recurse=True)

    for x in client.rmdir(l):
        print(x)


if __name__ == '__main__':
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
