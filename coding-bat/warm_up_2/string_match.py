# Problem


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0

def string_match(a, b):
    counter = 0
    if len(a) >= len(b):
        for item in range(len(b)):
            x = b[item:(item + 2)]
            y = a[item:(item + 2)]
            if len(x) == 2 and x == y:
                counter += 1
        return counter

    if len(b) >= len(a):
        for item in range(len(a)):
            x = b[item:(item + 2)]
            y = a[item:(item + 2)]
            if len(x) == 2 and x == y:
                counter += 1
        return counter


string_match('abc', 'abc')
