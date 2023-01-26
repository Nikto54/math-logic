from Checks import Checks


class Auxiliary:

    @staticmethod
    def is_checked(crit, position, crits):

        for index in range(position):

            if f'({crits[index]} -> {crit})' in crits:
                Checks.third(crits[index], crit)
                return True

        return False

    @staticmethod
    def is_tenth(string):

        if string.startswith('(!!'):
            new = string[3: (len(string) - 1)]
            lst = new.split(' -> ')

            if len(lst) % 2 == 0:
                left = ' -> '.join(lst[:(len(lst) // 2)])
                right = ' -> '.join(lst[(len(lst) // 2):])

                return str(left) == str(right), str(left)

            return False, '-1233'

        return False, '-1233'
