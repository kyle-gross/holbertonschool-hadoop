#!/usr/bin/env python3
"""This module contains the function createdir()"""

from snakebite.client import Client


def createdir(l):
    """Creates a directory from the path(s) `l`"""
    client = Client('127.0.1.1', 9000)

    for path in client.mkdir(l, create_parent=True):
        print(path)


if __name__ == '__main__':
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
