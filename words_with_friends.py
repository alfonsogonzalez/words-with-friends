#!/usr/bin/env python

from sys import exit, argv
from enchant import Dict
from itertools import permutations
from time import time as time

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
                
            if length == None:
                pass
            else:
                string = string[0:length]
                
            check = d.check(str(string))
            if check == True:
                if len(possibles) > 0:
                    for word in possibles:
                        if str(string) == str(word):
                            double = True
                            break
                        else:
                            double = False
                    if double == True:
                        pass
                    elif double == False:
                        possibles.append(string)
                        
                elif len(possibles) == 0:
                    possibles.append(string)
                    
            count += 1
            if count == 1000:
                print('Checked 1,000...')
            if count == 13000:
                print('Checked 13,000...')
            if count == 100000:
                print('Checked 100,000...')
            if count == 500000:
                print('Checked 500,000...')
    time2 = time()
    total_time = time2 - time1
    returns = {'possibles': possibles, 'count': count, 'time': total_time}
    return returns               

def main(argv):
    _prefix = prefix()
    _letters = letters()
    _suffix = suffix()
    _length = length()
    
    print('Checking all possibles combinations...')

    _possibles = check_if_word(letters=_letters, prefix=_prefix, suffix=_suffix, length=_length)

    print('Possible words:')
    for word in _possibles['possibles']:
        print(word)
    print('\n')
    print('Checked {} permutations ({} seconds)'.format(_possibles['count'], round(_possibles['time'], 5)))
          
if __name__ == '__main__':
    exit(main(argv))
