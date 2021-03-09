def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    new_list = []
    for num in nums:
        if num == 7:
            new_list = [num]
    return not not new_list

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

