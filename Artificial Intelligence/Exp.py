from PatMatch import *
from string import *

letters = ascii_lowercase + ascii_uppercase
operators = '+=*/%'
numbers = '0123456789'

student_rules = [
    ('find ?*a', ['To-find', '=', '?a']),
    ('?*a is equal to ?*b', ['?a', '=', '?b']),
    ('?*a is ?*b', ['?a', '=', '?b']),
    ('?*a plus ?*b', ['?a', '+', '?b']),
    ('?*a minus ?*b', ['?a', '-', '?b']),
    ('?*a divided by ?*b', ['?a', '/', '?b']),
    ('twice ?*a', ['2', '*', '?a']),
    ('sum ?*a and ?*b', ['?a', '+', '?b']),
    ('half ?*a', ['?a', '/', '2']),
    ('square ?*a', ['?a', '*', '?a']),
    ('difference between ?*a and ?*b', ['?b', '-', '?a']),
    ('?*a % less than ?*b', ['?b', '/', ['1', '-', ['?a', '/', 100]]])
]

def toeqstr(elst):
    ans = ''
    if type(elst) is str:
        return elst
    for item in elst:
        if type(item) is list:
            ans += "(" + toeqstr(item) + ")"
        else:
            if ans == '':
                ans = item
            else:
                ans += ' ' + str(item)
    return ans

def replace_item(n,o,lst):
    if lst == []:
        return []
    elif o == lst:
        return n
    elif type(lst) is not list:
        return lst
    else:
        ans = replace_item(n,o,lst[1:])
        ans.insert(0,replace_item(n,o,lst[0]))
        return ans

def translate_to_exp(eqwlst):
    print('Input: "', toeqstr(eqwlst), '"')
    for pattern, response in student_rules:
        pattern = pattern.split()
        bindings = match_pattern(pattern, eqwlst)

        if bindings:
            print('Rule: "', toeqstr(pattern), '", [', toeqstr(response), ']')
            print('Binding:', bindings)
            for var, val in bindings.items():
                tval = translate_to_exp(val)
                response = replace_item(tval, '?' + var,response)
            print('Output: ', response)
            return response
    if eqwlst == []:
        return eqwlst
    return eqwlst[0]

print(translate_to_exp('What is twice square z'.split()))


def in_exp(itm, lst):
    if type(lst) is str:
        return itm == lst
    elif lst == []:
        return False
    elif type(lst) is list:
        return in_exp(itm, lst[0]) or in_exp(itm, lst[1:])


def reverse_op(op):
    if op == '+':
        return '-'
    elif op == '-':
        return '+'
    elif op == '*':
        return '/'
    elif op == '/':
        return '*'
    elif op == '=':
        return '='


def isolate(var, eq):
    lhs = eq[0]
    op = eq[1]
    rhs = eq[2]

    if var == lhs:
        return eq
    elif var == rhs:
        return [rhs, op, lhs]
    elif type(lhs) is str:
        return isolate(var, [rhs, op, lhs])
    elif type(rhs) is list and op == '=' and in_exp(var,rhs):
        return isolate(var, [rhs, op, lhs])
    elif in_exp(var, lhs[0]):
        return isolate(var, [lhs[0], '=', [rhs, reverse_op(lhs[1]), lhs[2]]])
    elif lhs[1] == '+' or lhs[1] == '*':
        return isolate(var, [lhs[2], '=', [rhs, reverse_op(lhs[1]), lhs[0]]])
    else:
        return isolate(var, [lhs[2], '=', [lhs[0], lhs[1], rhs]])


def solve_equation(var, eq):
    eq2 = isolate(var, eq)
    # print(eq2)
    return eq2[0], str(eval(toeqstr(eq2[2])))


def solve_equations(eqs):
    # print(eqs)
    print('UNSOLVED EQUATIONS')
    print_equations(eqs)
    print('SOLVED EQUATIONS')
    solved = solve(eqs)
    print_equations(solved)


def one_unkown2(equation):
    c = 0
    var = None

    for item in equation:
        if type(item) is list:
            ans = one_unkown2(item)
            c += ans[1]
            if ans[1] != 0:
                var = ans[0]
        else:
            flag = False
            for ch in item:
                if ch in letters:
                    flag = True
            if flag == True:
                c += 1
                var = item
    # print('contain ', c, ' variables')
    return var, c


def find_one_unkowneq(eqs):
    for eq in eqs:
        ans = one_unkown2(eq)
        count = ans[1]
        var = ans[0]
        if count == 1:
            return var, eq
    return None, []


def solve(eqs, solved=[]):
    # print(solved)
    # print(eqs)
    if len(eqs) == 0:
        return solved
    ans = find_one_unkowneq(eqs)
    var = ans[0]
    eq = ans[1]
    if eq != [] and var is not None:
        sol = solve_equation(var, eq)
        value = sol[1]
        eqs.remove(eq)
        eqs = replace_item(value, var, eqs)
        solved.append([var, '=', value])
        temp = solve(eqs, solved)
        return temp
    return solved


def print_equations(eqs):
    for eq in eqs:
        print(toeqstr(eq))


def remove_noise(txt):
    nwords = ['a', 'the', 'number', 'of', 'this', 'if', 'that', 'and']
    for w in nwords:
        if txt.count(w) > 0:
            # txt.remove(w)
            # txt = list (filter(lambda a: a != w, txt))
            txt = [a for a in txt if a != w]
    return txt


def student():
    userinput = input('Enter statement: ')
    userinput = userinput.lower()
    engEqs = userinput.split('.')
    print(engEqs)
    eqs = []
    for engeq in engEqs:
        engeq = engeq.split()
        eqwlst = remove_noise(engeq)
        eq1 = translate_to_exp(eqwlst)
        eqs.append(eq1)
    eqs = [eq for eq in eqs if eq != []]
    # print(eqs)
    # for eq in eqs:
    #   print(toeqstr(eq))
    solve_equations(eqs)

def flat(eqs):
    if type(eqs) is list and len(eqs) == 1:
        if type(eqs[0]) is list:
            return flat(eqs[0])
    return eqs

while True:
    student()
