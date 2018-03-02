#!/usr/bin/python -tt

# DegParse1.py

import sys

def getDegradome(filename):
# Read in a degradome density file. Add gene names to each block of
# degradome entries and return it as a list.
    INfile = open(filename, 'rU')
    gene = ''
    degradome = []
    for line in INfile:
        if line.startswith('#'):
            pass
        elif line.find('@ID') >= 0:
            gene = line[4:-1]
            next(INfile)    #skip the next line (@LN...) 
        elif line == '\n':
            gene = ''
        elif line[-2].isdigit():
            degLine = gene + '\t' + line
            degradome.append(degLine)
    INfile.close()
    return degradome

def main():
    OUTfile = open('degParse1_out.txt', 'w')
    deg = getDegradome(sys.argv[1])
    for row in deg:
        OUTfile.write(row)
    OUTfile.close()

if __name__ == '__main__':
    main()
