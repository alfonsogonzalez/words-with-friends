#!/usr/bin/env python

from sys import exit, argv
from enchant import Dict
from itertools import permutations
from time import time as time
from random import uniform

def letters():
    _letters = input('Input letters you have: ')
    return _letters

def prefix():
    prompt = input('Prefix? (y/n): ')
    if prompt == 'y':
        _prefix = input('Input prefix: ')
        return _prefix
    else:
        return None

def suffix():
    prompt = input('Suffix? (y/n): ')
    if prompt == 'y':
        _suffix = input('Input suffix: ')
        return _suffix
    else:
        return None

def length():
    prompt = input('Specific length? (y/n): ')
    if prompt == 'y':
        length = int(input('Length?: '))
        return length
    else:
        return None
    
def check_if_word(letters, prefix=None, suffix=None, length=None):
    possibles = []
    count = 0
    iterations = 0
    d = Dict('en_US')
    time1 = time()
    length_check = len(letters) + 1
    for num in range(2, length_check):
        permute = permutations(letters, num)
        for arrangement in permute:
            if prefix == None and suffix == None:
                string = ''.join(arrangement)
                
            elif prefix != None and suffix == None:
                string = prefix
                string += ''.join(arrangement)

            elif prefix == None and suffix != None:
                string = ''.join(arrangement)
                string += suffix

            elif prefix != None and suffix != None:
                string = prefix
                string += ''.join(arrangement)
                string += suffix

            if length != None:
                string = string[0:length]
                
            check = d.check(str(string))
            if check == True:
                if len(possibles) > 0:
                    for word in possibles:
                        iterations += 1
                        if str(string) == str(word):
                            double = True
                            break
                        else:
                            double = False
                        
                    if double == False:
                        possibles.append(string)
                        
                elif len(possibles) == 0:
                    possibles.append(string)
                    
            count += 1
            iterations += 1

            odds = int(uniform(0,2))
            if odds == 0:
                quote1 = 'Beep bop boop..'
            elif odds == 1:
                quote1 = 'Doing computer stuff..'

            odds2 = int(uniform(0,2))
            if odds2 == 0:
                quote2 = 'Bop boop beep'
            if odds2 == 1:
                quote2 = 'Much computer things wow..'
            
            if count == 1000:
                print(quote1)
            if count == 5000:
                print(quote2)
            if count == 80000:
                print('Checked 80,000...')
            if count == 500000:
                print('Checked 500,000...')
            if count == 900000:
                print('Almost done...')
    time2 = time()
    total_time = time2 - time1
    returns = {'possibles': possibles, 'count': count, 'time': total_time, 'iterations':iterations}
    return returns               

def main(argv):
    _prefix = prefix()
    _letters = letters()
    _suffix = suffix()
    _length = length()
    
    print('Checking all possibles combinations...', '\n')

    _possibles = check_if_word(letters=_letters, prefix=_prefix, suffix=_suffix, length=_length)
    
    if len(_possibles['possibles']) == 0:
        print('No possible combinations :(')

    else:
        print('Possible words:')
        for word in _possibles['possibles']:
            print(word)
        
    print('Checked {} permutations ({} seconds)'.format(_possibles['count'], round(_possibles['time'], 5)))
    print('Iterated through', _possibles['iterations'], 'total combinations')
    
if __name__ == '__main__':
    exit(main(argv))
