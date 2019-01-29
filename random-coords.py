#
# Created by Ben Cynamon
# for Florida State University's 2018 iGEM team
# ( iGEM = 'International Genetically Engineered Machine [Competition]' )
#
# Special thanks to David Eisenstat
# https://stackoverflow.com/questions/42080607/how-to-select-distinct-random-points-in-grid
#


import random
import os
  
def samplegrid(rows, columns, samples):
        try:
                return [divmod(i, columns) for i in random.sample(range(rows * columns), samples)]
        except ValueError:
                print
                print bcolors.WARNING + '--  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --' + bcolors.ENDC
                print
                print'    Error! Your sample is larger than your well plate can hold.'
                print
                print bcolors.WARNING + '--  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --  --' + bcolors.ENDC
                print
                print'Technical explanation:'
                print

def triplicate(samplegrid_output):
     var = []
     num = 0
     alphabet = { 0 : 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10 : 'K', 
     11: 'L', 12 : 'M', 13 : 'N', 14 : 'O', 15 : 'P', 16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 
     20 : 'U', 21 : 'V', 22 : 'W', 23 : 'X', 24 : 'Y', 25 : 'Z' }
     for i in range(len(samplegrid_output)+1):
             if i == 0:
                     continue
             if i%3 == 0:
                num += 1
                if num % 2 != 0:
                        print bcolors.WARNING + 'Coordinate #', num, ' : ', '(', alphabet[(samplegrid_output[i-3][0])], ',', samplegrid_output[i-3][1], ')', '(', alphabet[(samplegrid_output[i-2][0])], ',', samplegrid_output[i-2][1], ')', '(', alphabet[(samplegrid_output[i-1][0])], ',', samplegrid_output[i-1][1], ')' + bcolors.ENDC
                else:
                        print'Coordinate #', num, ' : ', '(', alphabet[(samplegrid_output[i-3][0])], ',', samplegrid_output[i-3][1], ')', '(', alphabet[(samplegrid_output[i-2][0])], ',', samplegrid_output[i-2][1], ')', '(', alphabet[(samplegrid_output[i-1][0])], ',', samplegrid_output[i-1][1], ')'

if os.system('defaults read -g AppleInterfaceStyle') == 0:
        class bcolors:
                WARNING = '\033[93m'
                ENDC = '\033[0m'
else:
        class bcolors:
                WARNING = '\033[94m'
                ENDC = '\033[0m'



print
print '_______________________________________________________________'
print
print '_______________________ i G E M _ F S U _______________________'
print
print '_______________________________________________________________'
print
print '_______________ Well Plate Coordinate Generator _______________'
print
print '_______________________________________________________________'
print


print'How many rows? (default: 8)'
rows = raw_input('> ')
print
if not rows:
        rows = 8
rows = int(rows)

print'How many columns? (default: 12)'
columns = raw_input('> ')
print
if not columns:
        columns = 12
columns = int(columns)

print'How many samples?'
samples = raw_input('> ')
print
if not samples:
        while not samples:
                print'Error!'
                print'How many samples?'
                samples = raw_input('> ')
                print
samples = int(samples) * 3
        

print
triplicate(samplegrid(rows, columns, samples))
print