import os
import sys
import datetime

if len(sys.argv) != 4:
    print("Please enter three arguments: year month day. \nFor example, for Sept 2, 2018: python hack.py 2018 9 2")
    sys.exit()

year = int(sys.argv[1])
month = int(sys.argv[2])
day = int(sys.argv[3])
startDate = datetime.date(year, month, day)


def commitOnDate(date, numCommits):
    for i in range(numCommits):
        os.system('echo "." >> dots')
        os.system('git add dots')
        os.system('git commit --date {} -m "."'.format(date.isoformat()))


def writeLetters(letters):
    letterOffset = 0
    for letter in letters:
        for offset in letter:
            commitOnDate(
                startDate + datetime.timedelta(days=(letterOffset + offset)), 1)
        letterOffset += 35


letterH = [0, 1, 2, 3, 4, 5, 6, 10, 17, 21, 22, 23, 24, 25, 26, 27]
letterE = [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 17, 20, 21, 24, 27]
letterL = [0, 1, 2, 3, 4, 5, 6, 13, 20, 27]
letterO = [0, 1, 2, 3, 4, 5, 6, 7, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27]
wordHello = [letterH, letterE, letterL, letterL, letterO]

writeLetters(wordHello)
