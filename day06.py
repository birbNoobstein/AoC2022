# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:05:19 2022

@author: Ana
"""
from collections import Counter

def find(chars, x):
    for c in range(len(chars[0:-(x-1)])):
        counter = Counter(chars[c:c+x])
        if counter.most_common()[0][1] == 1:
            return c+x

def part1():
    with open('./data/day06.txt') as handle:
        chars = handle.readline().strip()
    print('Part 1:', find(chars, 4))
    return chars
    

def part2(chars):
    return find(chars, 14)
    

def main():
    p1 = part1()
    print('Part 2:', part2(p1))
        
if __name__ == '__main__':
    main()