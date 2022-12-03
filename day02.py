# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:47:29 2022

@author: Ana
"""

convert = {'A':'X',
           'B':'Y',
           'C':'Z'}

shape_score = {'X':1,
               'Y':2,
               'Z':3}

winners1 = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]

winners2 = {'A':'B',
            'B':'C',
            'C':'A'}

def part1():
    with open('./data/day02.txt') as handle:
        games = []
        for game in handle.readlines():
            games.append([g.strip() for g in game.strip().split(' ')])
       
    score = 0
    for game in games:
        if game[1] == convert[game[0]]:
            score += 3
        elif game in winners1:
            score += 6
            
        score += shape_score[game[1]]
            
    print('Part 1:', score)
    return games

def part2(games):
   score = 0
   for game in games:
       if game[1] == 'Z':
           score += 6 + shape_score[convert[winners2[game[0]]]]
       elif game[1] == 'Y':
           score += 3 + shape_score[convert[game[0]]]
       else:
           score += shape_score[convert[winners2[winners2[game[0]]]]]
   return score

def main():
    p1 = part1()
    print('Part 2:', part2(p1))
        
if __name__ == '__main__':
    main()