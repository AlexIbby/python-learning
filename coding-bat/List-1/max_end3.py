# Problem


# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.


# max_end3([1, 2, 3]) → [3, 3, 3]
# max_end3([11, 5, 9]) → [11, 11, 11]
# max_end3([2, 11, 3]) → [3, 3, 3]

def max_end3(nums):
    new_list = []
    if nums[0] > nums[-1]:
        for item in nums:
            x = nums[0]
            item = x
            new_list.append(item)
        return new_list
    elif nums[-1] > nums[-0]:
        for item in nums:
            y = nums[-1]
            item = y
            new_list.append(item)
        return new_list
    elif nums[-1] == nums[-0]:
        for item in nums:
            y = nums[-1]
            item = y
            new_list.append(item)
        return new_list
