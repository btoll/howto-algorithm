#def palindrome_number(n):
#    if n < 0:
#        return False
#
#    k = n
#    ret = 0
#    while k:
#        rem = k % 10
#        ret = ret * 10 + rem
#        k //= 10
#    return ret == n


def palindrome_number(n):
    # As discussed above, when x < 0, x is not a palindrome.
    # Also if the last digit of the number is 0, in order to be a palindrome,
    # the first digit of the number also needs to be 0.
    # Only 0 satisfy this property.
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    ret = 0
    # Now the question is, how do we know that we've reached the half of the number?
    # Since we divided the number by 10, and multiplied the reversed number by 10, when the original number
    # is less than the reversed number, it means we've processed half of the number digits.
    while n > ret:
        rem = n % 10
        ret = ret * 10 + rem
        n //= 10

    # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
    # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
    # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
    return n == ret or n == (ret // 10)


print(palindrome_number(12321))
