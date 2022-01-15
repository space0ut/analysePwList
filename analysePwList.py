#!/usr/bin/python
# coding=utf-8
# compatible with python 2.7 and python 3.x

__author__  = "Dennis Jung"
__version__ = "1.0"
__date__    = "14.02.2018"

import argparse
import re
import collections

analysedArray = []
patternDict = {
    'upper': '',
    'lower': '',
    'numeric': '',
    'special': ''
}


def setDataList(value):
    analysedArray.append(value)


def analyseLine(line):
    patternString = ""
    for char in line:
        if char.islower():
            patternString += patternDict['lower']
        elif char.isupper():
            patternString += patternDict['upper']
        elif char.isnumeric():
            patternString += patternDict['numeric']
        elif re.match(r'[\W]', char):
            patternString += patternDict['special']

    return patternString


def getList(pathToWordlist, unicd):
    wordList = open(pathToWordlist, "r")
    for line in wordList:
        if len(line.split(':')) == 2:
            setDataList(analyseLine(unicode(line.strip('\n').split(':')[1], unicd)))
        else:
            setDataList(analyseLine(unicode(line.strip('\n'), unicd)))

    wordList.close()
    return True


def sortAnalysedList():
    counter = collections.Counter(analysedArray)
    for value in counter:
        print("{} found {} times".format(value, counter[value]))


def setPatternDict(pattern):
    if pattern == "hashcat":
        patternDict['upper'] = '?u'
        patternDict['lower'] = '?l'
        patternDict['numeric'] = '?d'
        patternDict['special'] = '?s'
    elif pattern == "crunch":
        patternDict['upper'] = ','
        patternDict['lower'] = '@'
        patternDict['numeric'] = '%'
        patternDict['special'] = '^'
    # set your custom pattern here


def printHelpText():
    return("""
This script will go through a wordlist and analyse the pattern for each listet password.
You can choose between hashcat output pattern or crunch output pattern.
Default unicode is set to utf-8
You can give a easy list of words or a worlist in [username]:[password] pattern. Both options in a list are also possible.

[Hashcat format]:
?l = abcdefghijklmnopqrstuvwxyz
?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
?d = 0123456789
?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

[Crunch format (depending on your charset)]:
@  = abcdefghijklmnopqrstuvwxyz
,  = ABCDEFGHIJKLMNOPQRSTUVWXYZ
%  = 0123456789
^  = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

[Pattern options]
hashcat
crunch

for a more sortet output use this line of command:
python analysePwList.py -w [wordlist] -e [unicode] -p [pattern] | sort | uniq -c

    """)


def main():
    unicd = 'utf-8'

    parser = argparse.ArgumentParser(epilog=printHelpText(), formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-w', '--wordlist', help='Path and Filename of wordlist', required=True)
    parser.add_argument('-p', '--pattern', help='Output as hashcat or crunch pattern', required=True)
    parser.add_argument('-e', '--encoding', help='Encoding from wordlist', required=False)
    parser.add_argument('-s', '--sort', help='Show simple statistics about found patterns', required=False, action='store_true')
    args = parser.parse_args()

    setPatternDict(args.pattern)

    if args.encoding:
        unicd = args.encoding
    if getList(args.wordlist, unicd):
        if args.sort:
            sortAnalysedList()
        else:
            for analysedString in analysedArray:
                print("{}".format(analysedString))


if __name__ == "__main__":
    main()
