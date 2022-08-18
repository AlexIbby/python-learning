# Problem


# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    lower_a = a.lower()
    lower_b = b.lower()
    match_end_a = len(lower_a) * -1
    match_end_b = len(lower_b) * -1

    if lower_a[match_end_b:] == lower_b:
        return True
    if lower_b[match_end_a:] == lower_a:
        return True
    else:
        return False
