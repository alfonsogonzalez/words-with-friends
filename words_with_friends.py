#!/usr/bin/env python

from sys import exit, argv
import enchant
from itertools import permutations
from time import time as time

def letters():
    _letters = input('Input letters you have: ')
    return _letters    

def check_if_word(letters):
    possibles = []
    count = 0
    d = enchant.Dict('en_US')
    time1 = time()
    length = len(letters) + 1
    for num in range(2, length):
        permute = permutations(letters, num)
        for arrangement in permute:
            string = ''.join(arrangement)
            check = d.check(str(string))
            if check == True:
                possibles.append(string)
            count += 1
    time2 = time()
    total_time = time2 - time1
    returns = {'possibles': possibles, 'count': count, 'time': total_time}
    return returns               

def main(argv):
    _letters = letters()
    _possibles = check_if_word(_letters)
    print('Possible words:')
    for word in _possibles['possibles']:
        print(word)
    print('Checked {} permutations ({} seconds)'.format(_possibles['count'], round(_possibles['time'], 5)))
          
if __name__ == '__main__':
    exit(main(argv))
