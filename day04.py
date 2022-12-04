# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:28:39 2022

@author: Ana
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:31:53 2022

@author: Ana
"""

def part1():
    with open('./data/day04.txt') as handle:
        ID = []
        count = 0
        for group in handle.readlines():
            group = group.strip().split(',')
            ID.append(group)
            groupA = group[0].split('-')
            groupB = group[1].split('-')
            if int(groupB[0]) <= int(groupA[0]) and int(groupB[1]) >= int(groupA[1]):
                count +=1
            elif int(groupA[0]) <= int(groupB[0]) and int(groupA[1]) >= int(groupB[1]):
                count +=1
            
    print('Part 1:', count)
    return ID

def part2(groups):
    overlaps = 0
    for group in groups:
        groupA = group[0].split('-')
        groupB = group[1].split('-')
        if int(groupB[0]) <= int(groupA[0]) and int(groupB[1]) >= int(groupA[0]):
            overlaps += 1
        elif int(groupA[0]) <= int(groupB[0]) and int(groupA[1]) >= int(groupB[0]):
            overlaps += 1
    return overlaps
    

def main():
    p1 = part1()
    print('Part 2:', part2(p1))
        
if __name__ == '__main__':
    main()