# Problem


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    count = 0
    index1 = 0
    index2 = 4
    for item in range(len(str) - 1):
        code = str[index1:index2]
        if code[0:2] == "co" and code[3:4] == "e":
            count += 1
            index1 += 1
            index2 += 1

        else:
            index1 += 1
            index2 += 1
    return count
