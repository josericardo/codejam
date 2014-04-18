#!/usr/bin/env python
# coding=utf-8

import fileinput

data = (l for l in fileinput.input())
T = int(data.next())

def worth_build_another_farm(rate, C, F, X):
    time_to_reach_X = X / rate
    time_to_build_another_farm = C / rate
    time_to_reach_X_in_the_new_rate = X / (rate + F)

    return time_to_reach_X > time_to_build_another_farm + time_to_reach_X_in_the_new_rate

for i in xrange(1, T+1):
    C, F, X = [float(f) for f in data.next().split()]

    rate = 2.0 # cookies/sec
    elapsed_time = 0.0

    while worth_build_another_farm(rate, C, F, X):
        elapsed_time += C / rate # time to build another farm
        rate += F

    # by now I've burned all cookies building new farms
    elapsed_time += X / rate

    answer = elapsed_time
    print('Case #%d: %.7f' % (i, answer))
