# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:51:58 2022

@author: Ana
"""
import re
import copy

def scheme_parse(scheme_list):
    scheme = {}
    for k in scheme_list[0]:
        scheme.update({k:[l[int(k)-1] for l in scheme_list[1::] if l[int(k)-1] != ' ']})
    return scheme
        

def tops(scheme):
    crates = [scheme[k][-1] for k in scheme.keys()]
    return ''.join(crates)
    

def part1():
    start = []
    moves = []
    with open('./data/day05.txt') as handle:
        scheme = True
        for line in handle.readlines():
            if line == '\n':
                scheme = False
            elif scheme:
                line = re.split('', line.rstrip())
                line.pop(0)
                line.pop(0)
                start.append([line[i] for i in range(len(line)) if i%4 == 0])
            else:
                moves.append([line.rstrip().split()[i] for i in range(6) if i%2 != 0])
    start.reverse()
    scheme = scheme_parse(start)
    scheme2 = copy.deepcopy(scheme)
    
    for move in moves:
        for i in range(int(move[0])):
            scheme[move[2]].append(scheme[move[1]][-1])
            scheme[move[1]].pop(-1)
    print('Part 1:', tops(scheme))
    return moves, scheme2

def part2(moves, scheme):
    for move in moves:
        scheme[move[2]] += scheme[move[1]][-int(move[0])::]
        for i in range(int(move[0])):
            scheme[move[1]].pop(-1)
    return tops(scheme)


def main():
    moves, scheme = part1()
    print('Part 2:', part2(moves, scheme))


if __name__ == '__main__':
    main()