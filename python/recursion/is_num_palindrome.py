#def is_num_palindrome(num):
#    nums = []
#    while num:
#        nums.insert(0, num % 10)
#        num //= 10
#
#    i = 0
#    for j in range(len(nums) - 1, -1, -1):
#        if i > j:
#            return True
#        if nums[i] != nums[j]:
#            return False
#        i += 1


def is_num_palindrome(num):
    k = 0
    n = num
    while n:
        d = n % 10
        k = k * 10 + d
        n //= 10
    return k == num


print(is_num_palindrome(4213124))
