# Problem


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True

def xyz_there(str):
    xyz_count = str.count('xyz')
    xyz_dot_count = str.count('.xyz')
    net_xyz = xyz_count - xyz_dot_count
    if net_xyz > 0:
        return True
    else:
        return False
