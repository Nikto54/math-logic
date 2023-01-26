from Axioms import Axioms


class Checks:

    @staticmethod
    def first(line):
        crit = []

        print(line)
        crit.append(line)

        cur = Axioms.first(crit[0], f'!{line}')
        print(cur)
        crit.append(cur)

        cur = Checks.check_string(crit[0], cur)
        print(cur)
        crit.append(cur)

        cur = Axioms.first(f'!{line}', f'!{line}')
        print(cur)
        crit.append(cur)

        cur = Axioms.second(f'!{line}', f'(!{line} -> !{line})', f'!{line}')
        print(cur)
        crit.append(cur)

        cur = Checks.check_string(crit[3], cur)
        print(cur)
        crit.append(cur)

        cur = Axioms.first(f'!{line}', f'(!{line} -> !{line})')
        print(cur)
        crit.append(cur)

        cur = Checks.check_string(cur, crit[5])
        print(cur)
        crit.append(cur)

        cur = Axioms.ninth(f'!{line}', line)
        print(cur)
        crit.append(cur)

        cur = Checks.check_string(crit[2], cur)
        print(cur)
        crit.append(cur)

        cur = Checks.check_string(crit[7], cur)
        print(cur)
        crit.append(cur)

    @staticmethod
    def second(line):
        crit = [line]

        print(Axioms.first(line, f'!!{line}'))
        crit.append(Axioms.first(line, f'!!{line}'))

        print(Axioms.first(crit[1], f'!(!!{line} -> {crit[0]})'))
        crit.append(Axioms.first(crit[1], f'!(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[1], crit[2]))
        crit.append(Checks.check_string(crit[1], crit[2]))

        print(Axioms.first(f'!(!!{line} -> {crit[0]})', crit[0]))
        crit.append(Axioms.first(f'!(!!{line} -> {crit[0]})', crit[0]))

        print(Axioms.first(f'!(!!{line} -> {crit[0]})', f'!(!!{line} -> {crit[0]})'))
        crit.append(Axioms.first(f'!(!!{line} -> {crit[0]})', f'!(!!{line} -> {crit[0]})'))

        print(Axioms.first(f'!(!!{line} -> {crit[0]})',
                           f'(!(!!{line} -> {crit[0]}) -> !(!!{line} -> {crit[0]}))'))
        crit.append(Axioms.first(f'!(!!{line} -> {crit[0]})',
                                 f'(!(!!{line} -> {crit[0]}) -> !(!!{line} -> {crit[0]}))'))

        print(Axioms.second(f'!(!!{line} -> {crit[0]})',
                            f'(!(!!{line} -> {crit[0]}) -> !(!!{line} -> {crit[0]}))',
                            f'!(!!{line} -> {crit[0]})'))
        crit.append(Axioms.second(f'!(!!{line} -> {crit[0]})',
                                  f'(!(!!{line} -> {crit[0]}) -> !(!!{line} -> {crit[0]}))',
                                  f'!(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[5], crit[7]))
        crit.append(Checks.check_string(crit[5], crit[7]))

        print(Checks.check_string(crit[6], crit[8]))
        crit.append(Checks.check_string(crit[6], crit[8]))

        print(Axioms.ninth(crit[0], f'(!!{line} -> {crit[0]})'))
        crit.append(Axioms.ninth(crit[0], f'(!!{line} -> {crit[0]})'))

        print(Axioms.first(crit[10], f'!(!!{line} -> {crit[0]})'))
        crit.append(Axioms.first(crit[10], f'!(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[10], crit[11]))
        crit.append(Checks.check_string(crit[10], crit[11]))

        print(Axioms.second(f'!(!!{line} -> {crit[0]})', crit[1],
                            f'(({crit[0]} -> !(!!{line} -> {crit[0]})) -> !{line})'))
        crit.append(Axioms.second(f'!(!!{line} -> {crit[0]})', crit[1],
                                  f'(({crit[0]} -> !(!!{line} -> {crit[0]})) -> !{line})'))

        print(Checks.check_string(crit[3], crit[13]))
        crit.append(Checks.check_string(crit[3], crit[13]))

        print(Checks.check_string(crit[12], crit[14]))
        crit.append(Checks.check_string(crit[12], crit[14]))

        print(Axioms.second(f'!(!!{line} -> {crit[0]})', f'({crit[0]} -> !(!!{line} -> {crit[0]}))', f'!{line}'))
        crit.append(Axioms.second(f'!(!!{line} -> {crit[0]})', f'({crit[0]} -> !(!!{line} -> {crit[0]}))', f'!{line}'))

        print(Checks.check_string(crit[4], crit[16]))
        crit.append(Checks.check_string(crit[4], crit[16]))

        print(Checks.check_string(crit[15], crit[17]))
        crit.append(Checks.check_string(crit[15], crit[17]))

        print(Axioms.tenth(f'!{line}', crit[0]))
        crit.append(Axioms.tenth(f'!{line}', crit[0]))

        print(Axioms.first(crit[19], f'!(!!{line} -> {crit[0]})'))
        crit.append(Axioms.first(crit[19], f'!(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[19], crit[20]))
        crit.append(Checks.check_string(crit[19], crit[20]))

        print(Axioms.second(f'!(!!{line} -> {crit[0]})', f'!{line}', f'(!!{line} -> {crit[0]})'))
        crit.append(Axioms.second(f'!(!!{line} -> {crit[0]})', f'!{line}', f'(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[18], crit[22]))
        crit.append(Checks.check_string(crit[18], crit[22]))

        print(Checks.check_string(crit[21], crit[23]))
        crit.append(Checks.check_string(crit[21], crit[23]))

        print(Axioms.ninth(f'!(!!{line} -> {crit[0]})', f'(!!{line} -> {crit[0]})'))
        crit.append(Axioms.ninth(f'!(!!{line} -> {crit[0]})', f'(!!{line} -> {crit[0]})'))

        print(Checks.check_string(crit[24], crit[25]))
        crit.append(Checks.check_string(crit[24], crit[25]))

        print(Checks.check_string(crit[9], crit[26]))
        crit.append(Checks.check_string(crit[9], crit[26]))

    @staticmethod
    def third(line1, line2):
        crit = []

        print(Axioms.first(f'!{line2}', f'({line1} -> {line2})'))
        crit.append(Axioms.first(f'!{line2}', f'({line1} -> {line2})'))

        print(Axioms.first(f'!{line2}', line1))
        crit.append(Axioms.first(f'!{line2}', line1))

        print(Axioms.first(crit[1], f'!{line2}'))
        crit.append(Axioms.first(crit[1], f'!{line2}'))

        print(Checks.check_string(crit[1], crit[2]))
        crit.append(Checks.check_string(crit[1], crit[2]))

        print(Axioms.first(crit[1], f'({line1} -> {line2})'))
        crit.append(Axioms.first(crit[1], f'({line1} -> {line2})'))

        print(Axioms.first(crit[4], f'!{line2}'))
        crit.append(Axioms.first(crit[4], f'!{line2}'))

        print(Checks.check_string(crit[4], crit[5]))
        crit.append(Checks.check_string(crit[4], crit[5]))

        print(Axioms.second(f'!{line2}', crit[1], f'(({line1} -> {line2}) -> {crit[1]})'))
        crit.append(Axioms.second(f'!{line2}', crit[1], f'(({line1} -> {line2}) -> {crit[1]})'))

        print(Checks.check_string(crit[3], crit[7]))
        crit.append(Checks.check_string(crit[3], crit[7]))

        print(Checks.check_string(crit[6], crit[8]))
        crit.append(Checks.check_string(crit[6], crit[8]))

        print(Axioms.second(f'({line1} -> {line2})', f'!{line2}', f'({line1} -> !{line2})'))
        crit.append(Axioms.second(f'({line1} -> {line2})', f'!{line2}', f'({line1} -> !{line2})'))

        print(Axioms.first(crit[10], f'!{line2}'))
        crit.append(Axioms.first(crit[10], f'!{line2}'))

        print(Checks.check_string(crit[10], crit[11]))
        crit.append(Checks.check_string(crit[10], crit[11]))

        print(Axioms.second(f'!{line2}',
                            f'(({line1} -> {line2}) -> !{line2})',
                            f'((({line1} -> {line2}) -> (!{line2} -> ({line1} -> !{line2}))) -> (({line1} -> {line2}) -> ({line1} -> !{line2})))'))
        crit.append(Axioms.second(f'!{line2}',
                                  f'(({line1} -> {line2}) -> !{line2})',
                                  f'((({line1} -> {line2}) -> (!{line2} -> ({line1} -> !{line2}))) -> (({line1} -> {line2}) -> ({line1} -> !{line2})))'))

        print(Checks.check_string(crit[0], crit[13]))
        crit.append(Checks.check_string(crit[0], crit[13]))

        print(Checks.check_string(crit[12], crit[14]))
        crit.append(Checks.check_string(crit[12], crit[14]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!{line2} -> ({line1} -> !{line2})))',
                            f'(({line1} -> {line2}) -> ({line1} -> !{line2}))'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!{line2} -> ({line1} -> !{line2})))',
                                  f'(({line1} -> {line2}) -> ({line1} -> !{line2}))'))

        print(Checks.check_string(crit[9], crit[16]))
        crit.append(Checks.check_string(crit[9], crit[16]))

        print(Checks.check_string(crit[15], crit[17]))
        crit.append(Checks.check_string(crit[15], crit[17]))

        print(Axioms.ninth(line1, line2))
        crit.append(Axioms.ninth(line1, line2))

        print(Axioms.first(crit[19], f'!{line2}'))
        crit.append(Axioms.first(crit[19], f'!{line2}'))

        print(Checks.check_string(crit[19], crit[20]))
        crit.append(Checks.check_string(crit[19], crit[20]))

        print(Axioms.second(f'({line1} -> {line2})', f'({line1} -> !{line2})', f'!{line1}'))
        crit.append(Axioms.second(f'({line1} -> {line2})', f'({line1} -> !{line2})', f'!{line1}'))

        print(Axioms.first(crit[22], f'!{line2}'))
        crit.append(Axioms.first(crit[22], f'!{line2}'))

        print(Checks.check_string(crit[22], crit[23]))
        crit.append(Checks.check_string(crit[22], crit[23]))

        print(Axioms.second(f'!{line2}',
                            f'(({line1} -> {line2}) -> ({line1} -> !{line2}))',
                            f'((({line1} -> {line2}) -> (({line1} -> !{line2}) -> !{line1})) -> (({line1} -> {line2}) -> !{line1}))'))
        crit.append(Axioms.second(f'!{line2}',
                                  f'(({line1} -> {line2}) -> ({line1} -> !{line2}))',
                                  f'((({line1} -> {line2}) -> (({line1} -> !{line2}) -> !{line1})) -> (({line1} -> {line2}) -> !{line1}))'))

        print(Checks.check_string(crit[18], crit[25]))
        crit.append(Checks.check_string(crit[18], crit[25]))

        print(Checks.check_string(crit[24], crit[26]))
        crit.append(Checks.check_string(crit[24], crit[26]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (({line1} -> !{line2}) -> !{line1}))',
                            f'(({line1} -> {line2}) -> !{line1})'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (({line1} -> !{line2}) -> !{line1}))',
                                  f'(({line1} -> {line2}) -> !{line1})'))

        print(Checks.check_string(crit[21], crit[28]))
        crit.append(Checks.check_string(crit[21], crit[28]))

        print(Checks.check_string(crit[27], crit[29]))
        crit.append(Checks.check_string(crit[27], crit[29]))

        print(f'!!{line1}')
        crit.append(f'!!{line1}')

        print(Axioms.first(f'!!{line1}', f'!{line2}'))
        crit.append(Axioms.first(f'!!{line1}', f'!{line2}'))

        print(Checks.check_string(crit[31], crit[32]))
        crit.append(Checks.check_string(crit[31], crit[32]))

        print(Axioms.first(crit[31], f'({line1} -> {line2})'))
        crit.append(Axioms.first(crit[31], f'({line1} -> {line2})'))

        print(Axioms.first(crit[34], f'!{line2}'))
        crit.append(Axioms.first(crit[34], f'!{line2}'))

        print(Checks.check_string(crit[34], crit[35]))
        crit.append(Checks.check_string(crit[34], crit[35]))

        print(Axioms.second(f'!{line2}', f'!!{line1}', f'(({line1} -> {line2}) -> !!{line1})'))
        crit.append(Axioms.second(f'!{line2}', f'!!{line1}', f'(({line1} -> {line2}) -> !!{line1})'))

        print(Checks.check_string(crit[33], crit[37]))
        crit.append(Checks.check_string(crit[33], crit[37]))

        print(Checks.check_string(crit[36], crit[38]))
        crit.append(Checks.check_string(crit[36], crit[38]))

        print(Axioms.tenth(f'!{line1}', f'!({line1} -> {line2})'))
        crit.append(Axioms.tenth(f'!{line1}', f'!({line1} -> {line2})'))

        print(Axioms.first(crit[40], f'!{line2}'))
        crit.append(Axioms.first(crit[40], f'!{line2}'))

        print(Checks.check_string(crit[40], crit[41]))
        crit.append(Checks.check_string(crit[40], crit[41]))

        print(Axioms.first(crit[40], f'({line1} -> {line2})'))
        crit.append(Axioms.first(crit[40], f'({line1} -> {line2})'))

        print(Axioms.first(crit[43], f'!{line2}'))
        crit.append(Axioms.first(crit[43], f'!{line2}'))

        print(Checks.check_string(crit[43], crit[44]))
        crit.append(Checks.check_string(crit[43], crit[44]))

        print(Axioms.second(f'!{line2}', crit[40],
                            f'(({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2}))))'))
        crit.append(Axioms.second(f'!{line2}', crit[40],
                                  f'(({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2}))))'))

        print(Checks.check_string(crit[42], crit[46]))
        crit.append(Checks.check_string(crit[42], crit[46]))

        print(Checks.check_string(crit[45], crit[47]))
        crit.append(Checks.check_string(crit[45], crit[47]))

        print(Axioms.second(f'({line1} -> {line2})', f'!{line1}', f'(!!{line1} -> !({line1} -> {line2}))'))
        crit.append(Axioms.second(f'({line1} -> {line2})', f'!{line1}', f'(!!{line1} -> !({line1} -> {line2}))'))

        print(Axioms.first(crit[49], f'!{line2}'))
        crit.append(Axioms.first(crit[49], f'!{line2}'))

        print(Checks.check_string(crit[49], crit[50]))
        crit.append(Checks.check_string(crit[49], crit[50]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !{line1})',
                            f'((({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2})))) -> (({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2}))))'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !{line1})',
                                  f'((({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2})))) -> (({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2}))))'))

        print(Checks.check_string(crit[30], crit[52]))
        crit.append(Checks.check_string(crit[30], crit[52]))

        print(Checks.check_string(crit[51], crit[53]))
        crit.append(Checks.check_string(crit[51], crit[53]))

        print(
            Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2}))))',
                          f'(({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2})))'))
        crit.append(
            Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!{line1} -> (!!{line1} -> !({line1} -> {line2}))))',
                          f'(({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2})))'))

        print(Checks.check_string(crit[48], crit[55]))
        crit.append(Checks.check_string(crit[48], crit[55]))

        print(Checks.check_string(crit[54], crit[56]))
        crit.append(Checks.check_string(crit[54], crit[56]))

        print(Axioms.second(f'({line1} -> {line2})', f'!!{line1}', f'!({line1} -> {line2})'))
        crit.append(Axioms.second(f'({line1} -> {line2})', f'!!{line1}', f'!({line1} -> {line2})'))

        print(Axioms.first(crit[58], f'!{line2}'))
        crit.append(Axioms.first(crit[58], f'!{line2}'))

        print(Checks.check_string(crit[58], crit[59]))
        crit.append(Checks.check_string(crit[58], crit[59]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !!{line1})',
                            f'((({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2}))) -> (({line1} -> {line2}) -> !({line1} -> {line2})))'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !!{line1})',
                                  f'((({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2}))) -> (({line1} -> {line2}) -> !({line1} -> {line2})))'))

        print(Checks.check_string(crit[39], crit[61]))
        crit.append(Checks.check_string(crit[39], crit[61]))

        print(Checks.check_string(crit[60], crit[62]))
        crit.append(Checks.check_string(crit[60], crit[62]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2})))',
                            f'(({line1} -> {line2}) -> !({line1} -> {line2}))'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> (!!{line1} -> !({line1} -> {line2})))',
                                  f'(({line1} -> {line2}) -> !({line1} -> {line2}))'))

        print(Checks.check_string(crit[57], crit[64]))
        crit.append(Checks.check_string(crit[57], crit[64]))

        print(Checks.check_string(crit[63], crit[65]))
        crit.append(Checks.check_string(crit[63], crit[65]))

        print(f'!!({line1} -> {line2})')
        crit.append(f'!!({line1} -> {line2})')

        print(Axioms.first(crit[67], f'!{line2}'))
        crit.append(Axioms.first(crit[67], f'!{line2}'))

        print(Checks.check_string(crit[67], crit[68]))
        crit.append(Checks.check_string(crit[67], crit[68]))

        print(Axioms.first(crit[67], f'({line1} -> {line2})'))
        crit.append(Axioms.first(crit[67], f'({line1} -> {line2})'))

        print(Axioms.first(crit[70], f'!{line2}'))
        crit.append(Axioms.first(crit[70], f'!{line2}'))

        print(Checks.check_string(crit[70], crit[71]))
        crit.append(Checks.check_string(crit[70], crit[71]))

        print(Axioms.second(f'!{line2}', crit[67], f'(({line1} -> {line2}) -> {crit[67]})'))
        crit.append(Axioms.second(f'!{line2}', crit[67], f'(({line1} -> {line2}) -> {crit[67]})'))

        print(Checks.check_string(crit[69], crit[73]))
        crit.append(Checks.check_string(crit[69], crit[73]))

        print(Checks.check_string(crit[72], crit[74]))
        crit.append(Checks.check_string(crit[72], crit[74]))

        print(Axioms.ninth(f'({line1} -> {line2})', f'!({line1} -> {line2})'))
        crit.append(Axioms.ninth(f'({line1} -> {line2})', f'!({line1} -> {line2})'))

        print(Axioms.first(crit[76], f'!{line2}'))
        crit.append(Axioms.first(crit[76], f'!{line2}'))

        print(Checks.check_string(crit[76], crit[77]))
        crit.append(Checks.check_string(crit[76], crit[77]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !({line1} -> {line2}))',
                            f'((({line1} -> {line2}) -> {crit[67]}) -> !({line1} -> {line2}))'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> !({line1} -> {line2}))',
                                  f'((({line1} -> {line2}) -> {crit[67]}) -> !({line1} -> {line2}))'))

        print(Checks.check_string(crit[66], crit[79]))
        crit.append(Checks.check_string(crit[66], crit[79]))

        print(Checks.check_string(crit[78], crit[80]))
        crit.append(Checks.check_string(crit[78], crit[80]))

        print(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> {crit[67]})', f'!({line1} -> {line2})'))
        crit.append(Axioms.second(f'!{line2}', f'(({line1} -> {line2}) -> {crit[67]})', f'!({line1} -> {line2})'))

        print(Checks.check_string(crit[75], crit[82]))
        crit.append(Checks.check_string(crit[75], crit[82]))

        print(Checks.check_string(crit[81], crit[83]))
        crit.append(Checks.check_string(crit[81], crit[83]))

        print(Axioms.tenth(f'!({line1} -> {line2})', f'!{line1}'))
        crit.append(Axioms.tenth(f'!({line1} -> {line2})', f'!{line1}'))

        print(Axioms.first(crit[85], f'!{line2}'))
        crit.append(Axioms.first(crit[85], f'!{line2}'))

        print(Checks.check_string(crit[85], crit[86]))
        crit.append(Checks.check_string(crit[85], crit[86]))

        print(Axioms.second(f'!{line2}', f'!({line1} -> {line2})', f'({crit[67]} -> !{line1})'))
        crit.append(Axioms.second(f'!{line2}', f'!({line1} -> {line2})', f'({crit[67]} -> !{line1})'))

        print(Checks.check_string(crit[84], crit[88]))
        crit.append(Checks.check_string(crit[84], crit[88]))

        print(Checks.check_string(crit[87], crit[89]))
        crit.append(Checks.check_string(crit[87], crit[89]))

        print(Axioms.second(f'!{line2}', crit[67], f'!{line1}'))
        crit.append(Axioms.second(f'!{line2}', crit[67], f'!{line1}'))

        print(Checks.check_string(crit[69], crit[91]))
        crit.append(Checks.check_string(crit[69], crit[91]))

        print(Checks.check_string(crit[90], crit[92]))
        crit.append(Checks.check_string(crit[90], crit[92]))

        print(Axioms.ninth(f'!{line2}', f'!{line1}'))
        crit.append(Axioms.ninth(f'!{line2}', f'!{line1}'))

        print(Checks.check_string(crit[93], crit[94]))
        crit.append(Checks.check_string(crit[93], crit[94]))

        print(Checks.check_string(crit[33], crit[95]))
        crit.append(Checks.check_string(crit[33], crit[95]))

    @staticmethod
    def check_string(string, old_string):
        return old_string[len(string) + 5: len(old_string) - 1] if old_string.startswith(
            f'({string} -> ') else old_string
