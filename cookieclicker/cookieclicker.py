#!/usr/bin/env python
# coding=utf-8

import fileinput
import time
import numba

@numba.jit('f8(f8,i4,f8,f8)')
def elapsed_time(rate, C, F, X):
    elapsed_time = 0.0

    worth = True
    while worth:
        time_to_reach_X = X / rate
        time_to_build_another_farm = C / rate
        time_to_reach_X_in_the_new_rate = X / (rate + F)
        worth = time_to_reach_X > time_to_build_another_farm + time_to_reach_X_in_the_new_rate

        if worth:
            elapsed_time += C / rate # time to build another farm
            rate += F

    # by now I've burned all cookies building new farms
    return elapsed_time + (X / rate)

start = time.time()

data = (l for l in fileinput.input())
T = int(data.next())

for i in xrange(1, T+1):
    C, F, X = [float(f) for f in data.next().split()]

    rate = 2.0 # cookies/sec
    answer = elapsed_time(rate, C, F, X)
    #print('Case #%d: %.7f' % (i, answer))

print "Finished in ", time.time()-start, " secs."
