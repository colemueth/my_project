#!/usr/bin/python -tt

# DegParse.py
# Parses a CleaveLand-generated Degradome Density file
# for likely sliced transcripts, regardless of sRNA presence.
# Then compares two files for differences.

import sys

def getDegradome(filename):
# Read in a degradome density file. Add gene names to each block of
# degradome entries and return it as a list.
    INfile = open(filename, 'rU')
    gene = ''
    degradome = []
    for line in INfile:
        if line.startswith('#'): # ignore header comments
            pass
        elif line.find('@ID') >= 0: # cut off @ID and store gene name
            gene = line[4:-1]
            next(INfile)    #skip the next line (@LN...) 
        elif line == '\n':
            gene = ''
        elif line[-2].isdigit():
            degLine = gene + '\t' + line
            degradome.append(degLine)
    INfile.close()
    return degradome

# establishes the "negative" cases, where >=n reads are present at a given
# location in uninfected.
def uninfected():
    degU = getDegradome(sys.argv[1])
    Ulist = []
    for urow in degU:
        rowList = urow.split()
        if int(rowList[2]) >= 3:
            Ulist.append(str(rowList[0] + '\t' + rowList[1]))
    return Ulist

# establishes the "positive" cases, where >=n reads are present at a given
# location in infected, and that is the highest peak for that transcript.
def infected():
    degI = getDegradome(sys.argv[2])
    Ilist = []
    for irow in degI:
        rowList = irow.split()
        if int(rowList[2]) >=20 and int(rowList[3]) == 0:
            Ilist.append(str(rowList[0] + '\t' + rowList[1]))
    return Ilist

def main():     
    OUTfile = open('ParseOut15.txt', 'w') 
    degU = uninfected()
    print(len(degU))
    degI = infected()
    print(len(degI))
    for i in degI:
        if i not in degU:
            OUTfile.write(i + '\n')
    OUTfile.close()

if __name__ == '__main__':
    main()

# Next steps for development:
# It's not very user friendly
# It's not very fast
# consider int(rowList[3]) == 0 or 2
# move last for loop to a new function called 'parse' 
# and make a UI for main()

