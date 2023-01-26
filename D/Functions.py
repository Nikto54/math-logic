class Functions:
    row, position, el = '', 0, ''

    def find(self, symbol):
        if self.row.startswith(symbol, self.position):
            self.position += len(symbol)
            return True

        return False

    def imp(self):
        self.el = self.dis()

        if self.find('->'):
            self.el = f'({self.el} -> {self.imp()})'

        return self.el

    def dis(self):
        self.el = self.conj()

        while self.find('|'):
            self.el = f'({self.el} | {self.conj()})'

        return self.el

    def conj(self):
        self.el = self.neg()

        while self.find('&'):
            self.el = f'({self.el} & {self.neg()})'

        return self.el

    def neg(self):

        if self.find('('):
            self.el = self.imp()
            self.find(')')

            return self.el

        if self.find('!'):
            return f'!{self.neg()}'

        self.el = ''

        while self.row[self.position].isalpha() \
                or self.row[self.position].isdigit() \
                or self.row[self.position] in "'":
            self.el += self.row[self.position]

            self.position += 1

        return self.el

    def rev(self, row):
        self.row = f'{row}#'
        self.position = 0

        return self.imp()
