#
# Created by Ben Cynamon
# for Florida State University's 2018 iGEM team
# ( iGEM = 'International Genetically Engineered Machine [Competition]' )
#
# Special thanks to David Eisenstat
# https://stackoverflow.com/questions/42080607/how-to-select-distinct-random-points-in-grid
#


import random

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
     for i in range(len(samplegrid_output)+1):
             if i == 0:
                     continue
             if i%3 == 0:
                num += 1
                if num % 2 == 0:
                        print bcolors.WARNING + 'Coordinate #', num, ' : ', samplegrid_output[(i-3):i], bcolors.ENDC
                else:
                        print'Coordinate #', num, ' : ', samplegrid_output[(i-3):i]

class bcolors:
    WARNING = '\033[93m'
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