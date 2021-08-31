'''
Time limit: 1.00 s Memory limit: 512 MB
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome
(i.e., it reads the same forwards and backwards).

Input

The only input line has a string of length n consisting of characters A–Z.

Output

Print a palindrome consisting of the characters of the original string.
You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints
1≤n≤106
Example

Input:
AAAACACBA

Output:
AACABACAA
'''


def solution_12():
    s = input()
    temp = set()
    res = list()
    for e in s:
        if e in temp:
            res.append(e)
            temp.remove(e)
        else:
            temp.add(e)
    if len(temp) > 1:
        print('NO SOLUTION')
    else:
        if temp:
            result = ''.join(res) + temp.pop() + ''.join(res[::-1])
        else:
            result = ''.join(res) + ''.join(res[::-1])
        print(result)


solution_12()
