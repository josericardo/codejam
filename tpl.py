#!/usr/bin/env python
# coding=utf-8

import fileinput

data = (l for l in fileinput.input())
T = int(data.next())

for d in data:
    print(d)
