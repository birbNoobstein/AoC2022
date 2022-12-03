# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:31:53 2022

@author: Ana
"""

def part1():
    with open('./data/day01.txt') as handle:
        elves = [0]
        for w in handle.readlines():
            if w == '\n':
                elves.append(0)
            else:
                elves[-1] = elves[-1] + int(w.strip())
    print('Part 1:', max(elves))
    return elves

def part2(elves):
    top = 0
    for i in range(3):
        top = top + max(elves)
        elves.remove(max(elves))
    return top
    

def main():
    p1 = part1()
    print('Part 2:', part2(p1))
        
if __name__ == '__main__':
    main()