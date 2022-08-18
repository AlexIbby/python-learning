# Problem


# Return the number of times that the string "hi" appears anywhere in the given string.


# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    index1 = 0
    index2 = 2
    counter = 0
    list = []
    list.append(str)
    check = str[index1:index2]
    while index2 < (len(str) + 2):
        if str[index1:index2] == "hi":
            index1 += 1
            index2 += 1
            counter += 1
        if str[index1:index2] != "hi":
            index1 += 1
            index2 += 1
    return(counter)
