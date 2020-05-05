#!/usr/bin/python3
"""
Given an array arr[] of N positive elements,
the task is to return the maximum sum of two numbers whose digits add up to an equal sum.
if there are no two numbers whose digits have equal sum, return -1.
"""
def solution(A):
    isum = {k:sum(int(i) for i in str(k)) for k in A}
    if len(isum.values()) == len(set(isum.values())):
        return -1
    d = {}
    for v in isum.values():
        if v not in d:
            d[v] = [k for k in isum.keys() if v == isum[k]]
    l = []
    for v in d.values():
        if len(v) == 2:
            l.append(v)
        elif len(v) > 2:
            setv = set(v)
            v = list(setv)
            for i in range(len(v) - 1):
                for s in range(i + 1, len(v)):
                    l.append([v[i], v[i + 1]])
    sums = []
    for i in l:
        sums.append(sum(i))
    return max(sums)
