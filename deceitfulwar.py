#!/usr/bin/env python
# coding=utf-8

import fileinput

data = (l for l in fileinput.input())
T = int(data.next())

for i in xrange(1, T+1):
    data.next()
    naomis = sorted([float(f) for f in data.next().split()])
    kens = sorted([float(f) for f in data.next().split()])

    pairings = zip(naomis, kens)
    print(pairings)
    deceitful_points = 0

    deceitful_points = sum(1 for p in pairings if p[0] > p[1])
    war_points = sum(1 for p in naomis if sum(1 for k in kens if p < k) == 0)

    print('Case #%d: %d %d' % (i, deceitful_points, war_points))
