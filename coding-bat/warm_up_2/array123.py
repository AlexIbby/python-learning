# Problem


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
    x = [1, 2, 3]
    index1 = 0
    index2 = 3

    while index2 <= (len(nums) + 1):
        check = nums[index1:index2]
        if check == x:
            return True
        else:
            index1 += 1
            index2 += 1

    return False
