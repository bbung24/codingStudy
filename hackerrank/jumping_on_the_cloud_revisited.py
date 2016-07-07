#/usr/bin/env python
"""
Aerith is playing a cloud game! In this game, there are n clouds numbered 
sequentially from 0 to n-1. Each cloud is either an ordinary cloud or a 
thundercloud. 

Aerith starts out on cloud 0 with energy level E = 100. She can use 1 unit
of energy to make a jump of size k to cloud (i+k) % n untill she gets back
to cloud 0. If Aerith lands on a thundercloud, her energy(E) decreases by 2
additional units. The game ends when Aerith lands back on cloud 0.

Given the values of n, k, and the configuration of the clouds, can you
determine the final value of E after the game ends?

Note: Recall that % refers to the modulo operation.

E = 100
1 energy = (i+k) % n
"""
import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

def decrease_energy(E, c):
    if c == 0:
        E -= 1
    else:
        E -= 3
    return E

def find_energy(c, n, k):
    E = 100
    index = (0+k) % n
    if index == 0:
        E = decrease_energy(E, c[index])
        return E
    else:
        E = decrease_energy(E, c[index])
    while index != 0:
        index = (index+k) % n
        E = decrease_energy(E, c[index])
    return E

print find_energy(c, n, k)