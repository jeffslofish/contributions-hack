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


def all_letters():
    return {
        "a": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
        ],
        "b": [
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
        ],
        "c": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "d": [
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
        ],
        "e": [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        "f": [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        "g": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "h": [
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
        ],
        "i": [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
        ],
        "j": [
            [1, 1, 1, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "k": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
        "l": [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 1, 1],
        ],
        "m": [
            [1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ],
        "n": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1],
        ],
        "o": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "p": [
            [1, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        "q": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
        ],
        "r": [
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [1, 0, 0, 0, 1],
        ],
        "s": [
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "t": [
            [1, 1, 1, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ],
        "u": [
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 0],
        ],
        "v": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ],
        "w": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0],
        ],
        "x": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
        ],
        "y": [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ],
        "z": [
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
    }


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


def generate_offset_list(letter):
    rows = len(letter)
    cols = len(letter[0])

    offset_list = []
    for i in range(rows):
        for j in range(cols):
            if letter[i][j]:
                offset_list.append(rows * j + i)

    return sorted(offset_list)


def test_print_letter(letter):
    rows = len(letter)
    cols = len(letter[0])

    for i in range(rows):
        for j in range(cols):
            print("#", end="") if letter[i][j] else print(" ", end="")
        print()


letters = all_letters()

letterA = generate_offset_list(letters["a"])
letterB = generate_offset_list(letters["b"])
letterC = generate_offset_list(letters["c"])
letterD = generate_offset_list(letters["d"])
letterF = generate_offset_list(letters["f"])
letterG = generate_offset_list(letters["g"])
letterI = generate_offset_list(letters["i"])
letterJ = generate_offset_list(letters["j"])
letterK = generate_offset_list(letters["k"])
letterM = generate_offset_list(letters["m"])
letterN = generate_offset_list(letters["n"])
letterO = generate_offset_list(letters["o"])
letterP = generate_offset_list(letters["p"])
letterQ = generate_offset_list(letters["q"])
letterR = generate_offset_list(letters["r"])
letterS = generate_offset_list(letters["s"])
letterT = generate_offset_list(letters["t"])
letterU = generate_offset_list(letters["u"])
letterV = generate_offset_list(letters["v"])
letterW = generate_offset_list(letters["w"])
letterX = generate_offset_list(letters["x"])
letterY = generate_offset_list(letters["y"])
letterZ = generate_offset_list(letters["z"])

letterH = [0, 1, 2, 3, 4, 5, 6, 10, 17, 21, 22, 23, 24, 25, 26, 27]
letterE = [0, 1, 2, 3, 4, 5, 6, 7, 10, 13, 14, 17, 20, 21, 24, 27]
letterL = [0, 1, 2, 3, 4, 5, 6, 13, 20, 27]
letterO = [0, 1, 2, 3, 4, 5, 6, 7, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27]
wordHello = [letterH, letterE, letterL, letterL, letterO]

writeLetters(wordHello)
