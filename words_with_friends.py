#!/usr/bin/env python

from sys import exit, argv
from enchant import Dict
from itertools import permutations
from time import time
from random import uniform

class Info:
    def __init__(self, possibles, count, total_time, iterations):
        self.possibles = possibles
        self.count = count
        self.total_time = total_time
        self.iterations = iterations

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
    
def check_word(letters, prefix=None, suffix=None, length=None):
    possibles = []
    count = 0
    iterations = 0
    d = Dict('en_US')
    time1 = time()
    length_check = len(letters) + 1
    for num in range(4, length_check):
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
            if check:
                if len(possibles) > 0:
                    for word in possibles:
                        iterations += 1
                        if str(string) == str(word):
                            double = True
                            break
                        else:
                            double = False
                        
                    if not double:
                        possibles.append(string)
                        
                elif len(possibles) == 0:
                    possibles.append(string)
                    
            count += 1
            iterations += 1

            if count == 1000:
                quotes_1 = ['Beep bop boop..', 'Doing computer stuff..', 'Such fast, very computer..']
                quote1 = quotes_1[int(uniform(0,3))]
                print(quote1)
                
            if count == 5000:
                quotes_2 = ['Bop boop beep..', 'Insert computer noises here..', 'Much computer things, wow..']
                quote2 = quotes_2[int(uniform(0,3))] 
                print(quote2)
                
            if count == 49000:
                quotes_3 = ['very computer..', 'doge would be proud', 'froge is the future']
                quote3 = quotes_3[int(uniform(0,3))]
                print(quote3)

    time2 = time()
    total_time = time2 - time1

    info = Info(possibles, count, total_time, iterations)
    return info              

def main(argv):
    _prefix = prefix()
    _letters = letters()
    _suffix = suffix()
    _length = length()
    
    print('Checking all possibles combinations...\n')

    _possibles = check_word(letters=_letters, prefix=_prefix, suffix=_suffix, length=_length)
    
    if len(_possibles.possibles) == 0:
        print('No possible combinations :(')

    else:
        print('Possible words:')
        for word in _possibles.possibles:
            print(word)
    print()
        
    print('Permutations checked: ', _possibles.count)
    print('Total iterations: ', _possibles.iterations)
    print('Total time (seconds): ', round(_possibles.time, 5))
    print()
    
if __name__ == '__main__':
    exit(main(argv))
