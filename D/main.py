from Functions import Functions
from Checks import Checks
from Auxiliary import Auxiliary


def main():
    st_sym = ''

    line = input()

    if not line or not line.replace(' ', '').replace('\n', '').replace('\t', '') \
            or line.replace(' ', '').replace('\n', '').replace('\t', '') == '|-' or '|-' not in line:
        return

    if line.startswith('|-'):
        hyp = ''
        crit_str = line[2:].replace(' ', '').replace('\n', '').replace('\t', '')
        hyps = []

    else:
        hyp = f'{line.split("|-")[0]} ' if line.split("|-")[0][-1] != ' ' else line.split("|-")[0]
        crit_str = line.split("|-")[1].replace(' ', '').replace('\n', '').replace('\t', '') if len(line.split("|-")) != 1 else ''
        hyps = line.split("|-")[0].split(', ') if ', ' in line.split("|-")[0] else [line.split("|-")[0]]

    crits = []
    crit = input()

    if not crit or not crit.replace(' ', '').replace('\n', '').replace('\t', ''):
        return

    crit = crit.replace(' ', '').replace('\n', '').replace('\t', '')

    fun = Functions()

    while crit != crit_str:

        if crit and crit not in crits:
            crits.append(fun.rev(crit))

        try:
            crit = input()

        except BaseException:
            break

        if not crit or not crit.replace(' ', '').replace('\n', '').replace('\t', ''):
            break

        crit = crit.replace(' ', '').replace('\n', '').replace('\t', '')

    if crit and crit not in crits:
        crits.append(fun.rev(crit))

    if crit_str:
        print(f'{hyp}|- !!{fun.rev(crit_str)}')

    for index, elem in enumerate(crits):

        if elem in hyps:
            Checks.first(elem)

        elif not Auxiliary.is_checked(elem, index, crits[:-1]):
            check, new_sym = Auxiliary.is_tenth(elem)

            st_sym = new_sym if new_sym != '-1233' else st_sym

            if check:
                Checks.second(st_sym)
            else:
                Checks.first(elem)


if __name__ == '__main__':
    main()
