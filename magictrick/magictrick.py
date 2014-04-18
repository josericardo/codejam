#!/usr/bin/env python
# coding=utf-8

import fileinput

data = (l for l in fileinput.input())
T = int(data.next())

for i in xrange(1, T+1):
    first_answer = int(data.next())
    first_cards = [data.next().split() for _ in range(0, 4)]
    second_answer = int(data.next())
    second_cards = [data.next().split() for _ in range(0, 4)]

    first_row = set(first_cards[first_answer-1])
    second_row = set(second_cards[second_answer-1])

    cards_in_both_rows = first_row & second_row

    if not cards_in_both_rows:
        answer = 'Volunteer cheated!'
    elif len(cards_in_both_rows) == 1:
        answer = list(cards_in_both_rows)[0]
    else:
        answer = 'Bad magician!'

    print('Case #{}: {}'.format(i, answer))
