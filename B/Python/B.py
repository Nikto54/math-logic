delims = ['!', '|', '-', '&', '(', ')']

def getAns(s):
    res = getResTable(s)
    c_0 = res.count(0)
    c_1 = res.count(1)

    if c_0 == 0:
        print("Valid")
    elif c_1 == 0:
        print("Unsatisfiable")
    else:
        print(f"Satisfiable and invalid, {c_1} true and {c_0} false cases")

def getResTable(s):
    mass, table = getRpn(s), parse(s)[1]
    a = []

    for i in range(0, len(mass)):
        if mass[i].isdigit():
            a.append(table[int(mass[i])])

        elif mass[i] == '!':
            a1 = a.pop()
            a.append(negative(a1))

        else:
            a2 = a.pop()
            a1 = a.pop()
            a.append(calc(a1, a2, mass[i]))

    try:
        return a.pop()
    except:
        return [0]

def getRpn(s):
    mass = parse(s)[0]
    opers = []
    ans = []

    for ch in mass:
        if ch == '(':
            opers.append(ch)

        elif ch in delims:
            if not opers:
                opers.append(ch)

            elif ch == ')':
                while True:
                    curr = opers[len(opers) - 1]
                    opers.pop()

                    if curr == '(':
                        break
                    ans.append(curr)

            elif getPrior(opers[len(opers) - 1]) <= getPrior(ch):
                opers.append(ch)

            else:
                while True:
                    if not opers:
                        break

                    curr = opers[len(opers) - 1]
                    if getPrior(curr) <= getPrior(ch):
                        break

                    ans.append(curr)
                    opers.pop()
                opers.append(ch)

        else:
            ans.append(ch)

    while opers:
        curr = opers[len(opers) - 1]
        ans.append(curr)
        opers.pop()

    return ans

def parse(s):
    mass = []
    for i in range(0, len(s)):
        a = s[i]
        for j in a:
            mass.append(j)

    ans = []
    curr = ''
    massOfVars = []

    for i in range(0, len(mass)):
        if mass[i] == '>':
            curr = ''

        elif mass[i] not in delims:
            curr += mass[i]

        else:
            ans.append(curr)
            massOfVars.append(curr)
            curr = ''

        if mass[i] in delims:
            ans.append(mass[i])

    ans.append(curr)
    massOfVars.append(curr)

    while ans.count(''):
        ans.remove('')

    while massOfVars.count(''):
        massOfVars.remove('')

    massOfVars = list(set(massOfVars))
    massOfVars.sort()

    for i in range(0, len(massOfVars)):
        for j in range(0, len(ans)):
            if massOfVars[i] == ans[j]:
                ans[j] = str(i)

    truthTable = createTable(len(massOfVars))

    return ans, truthTable

def calc(A, B, oper):
    ans = []
    if oper == '-':
        for i in range(0, len(A)):
            if A[i] <= B[i]:
                ans.append(1)

            else:
                ans.append(0)
    elif oper == '&':
        for i in range(0, len(A)):
            if A[i] == B[i] and A[i] != 0:
                ans.append(1)

            else:
                ans.append(0)
    elif oper == '|':
        for i in range(0, len(A)):
            if A[i] == 1 or B[i] == 1:
                ans.append(1)

            else:
                ans.append(0)

    return ans

def negative(A):
    neg = []
    for i in range(0, len(A)):
        if A[i] == 1:
            neg.append(0)

        else:
            neg.append(1)

    return neg

def getPrior(s):
    if s == '(':
        return 0
    elif s == '-':
        return 1
    elif s == '|':
        return 2
    elif s == '&':
        return 3
    elif s == '!':
        return 4

def createTable(size):
    table = []
    for i in range(0, size):
        table.append(([0] * ((2 ** size) // (2 ** (i + 1))) + [1] * ((2 ** size) // (2 ** (i + 1)))) * 2 ** (i))

    return table

def main():
    s = input()
    s = s.replace(" ", "").replace("!!", "").replace("\t", "").replace("\r", "").split(" ")

    getAns(s)

if __name__ == '__main__':
    main()
