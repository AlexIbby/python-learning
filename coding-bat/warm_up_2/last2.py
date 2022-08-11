# Problem


# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

def last2(str):

    ctr = 0
    compStr = str[len(str) - 2: len(str)]  # Taking advantage of Python

    for i in range(0, len(str) - 2, 1):  # i < len(str) - 2, i < 6 - 2 = 4
        if str[i:i + 2] == compStr:
            ctr = ctr + 1

    return ctr
