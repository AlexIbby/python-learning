# Problem


# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
    x = [a, b, c]
    z = []

    if a != b and a != c:
        z.append(a)

    if b != c and b != a:
        z.append(b)

    if c != b and c != a:
        z.append(c)

    return sum(z)
