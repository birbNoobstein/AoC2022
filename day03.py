# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 22:56:29 2022

@author: Ana
"""
from collections import Counter

def part1():
    with open('./data/day03.txt') as handle:
        bags1 = []
        bags2 = []
        for b in handle.readlines():
            b = b.strip()
            bags1.append([b[0:int(len(b)/2)], b[int(len(b)/2):len(b)]])
            bags2.append(b)
            
    score = 0
    for bag in bags1:
        b1 = Counter(bag[0])
        b2 = Counter(bag[1])
        intersect = list(set(b1.keys()).intersection(b2.keys()))[0]
        score += 1 + ord(intersect.lower()) - ord('a')
        if intersect.isupper():
            score += 26
        
    print('Part 1:', score)
    return bags2

def part2(bags):
    score = 0
    for b in range(0, len(bags), 3):
        bag1 = Counter(bags[b])
        bag2 = Counter(bags[b+1])
        bag3 = Counter(bags[b+2])
        intersect = list(set(bag1.keys()).intersection(bag2.keys()))
        intersect = list(set(intersect).intersection(bag3.keys()))[0]
        score += 1 + ord(intersect.lower()) - ord('a')
        if intersect.isupper():
            score += 26
    return score
    

def main():
    p1 = part1()
    print('Part 2:', part2(p1))
        
if __name__ == '__main__':
    main()