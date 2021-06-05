def luhns(test):
    test = test.replace("-", "")

    if len(test) != 11:
        return False

    cc = list(map(int, test))
    check_index = cc.pop()
    cc = cc[::-1]
    res = 0
    for i, num in enumerate(cc):
        if i % 2 == 0:
            num = num << 1
            if num > 9:
                num -= 9
        res += num
    return (res + check_index) % 10 == 0

#    if test.islower() or test.isupper():
#        return False
#
#    S_prime = list("".join(test.split("-")))
#    S_prime = [int(x) for x in S_prime]
#    check_index = S_prime.pop(-1)
#    S_rev = S_prime[::-1]
#    for s in range(len(S_rev)):
#        if s % 2 == 0:
#            S_rev[s] = S_rev[s] * 2
#            if S_rev[s] > 9:
#                S_rev[s] -= 9
#
#    result = sum(S_rev) + check_index
#    return result % 10 == 0

s = "7992-7398-713"
#s = "78827398713"
print(luhns(s))
