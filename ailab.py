from math import *
from random import *

def count(l, c = 0):
    print(l, c)

    if l == []:
        return c

    if type(l[0]) == type([]):
        c += count(l[0])
    else:
        c += 1

    return count(l[1:], c)

# print(count([1,2,3,[5,6,3,[3,2,1],1],2,3]))

def member(a, l):
    print(l)

    if l == []:
        return False

    if type(l[0]) == type([]):
        return member(a, l[0]) or member(a, l[1:])

    if l[0] == a:
        return True

    return member(a, l[1:])

# print(member(10, [20,30,[50,60,10],60]))

def sum(l, s = 0):
    print(l, s)

    if l == []:
        return s

    if type(l[0]) == type([]):
        s += sum(l[0])
    else:
        s += l[0]

    return sum(l[1:], s)

# print(sum([1,2,3,[5,3,2,[1,10]],2]))

def delete(a, l, i = 0):
    print(l, i)

    if i >= len(l):
        return l

    if type(l[i]) == type([]):
        l.append(delete(a, l[i], 0))
        i += 1
    elif l[i] == a:
        l.remove(l[i])
    else:
        i += 1

    return delete(a, l[i:], i)

# print(delete(3, [1,2,3,4,5,[3,2,1],5]))

def substitute(a,b,l,ans = []):
    print(l, ans)

    if l == []:
        return ans

    if type(l[0]) == type([]):
        ans.append(substitute(a,b,l))
    elif l[0] == a:
        ans.append(b)

    ans.append(l[0])
    return substitute(a,b,l[1:])

# print(substitute(3,2,[1,2,3,4[3,2]]))

def reverse(l = [], i = 0):
    if i >= len(l):
        return l

    if type(l) == type([]):
        l.append(reverse(l[0]))
    else:
        l.append(l[0])

    i += 1
    reverse(l, i)

print(reverse([1,2,3,4]))


