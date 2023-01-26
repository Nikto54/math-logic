class Axioms:

    @staticmethod
    def first(val1, val2):
        return f'({val1} -> ({val2} -> {val1}))'

    @staticmethod
    def second(val1, val2, val3):
        return f'(({val1} -> {val2}) -> (({val1} -> ({val2} -> {val3})) -> ({val1} -> {val3})))'

    @staticmethod
    def ninth(val1, val2):
        return f'(({val1} -> {val2}) -> (({val1} -> !{val2}) -> !{val1}))'

    @staticmethod
    def tenth(val1, val2):
        return f'({val1} -> (!{val1} -> {val2}))'
