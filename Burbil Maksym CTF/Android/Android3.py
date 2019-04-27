decoded = [0x69, 0xA7, 0x55, 0xF3, 3, 0x60, 0x4F,
           0xA6, 0xB5, 0x35, 0xC3, 0xE0, 0x89, 0x46]

mask = [0xad, 0x3a, 0x12, 0x90, 0x19, 0x99, 0xad,
        0x3a, 0x12, 0x90, 0x19, 0x99, 0xad, 0x3a]

maxval = 0xFFFFFFFF


def deadbeef(r2: 'symbol', r1: 'will inflict shifts'):
    temp1 = (r2 << r1) & maxval
    r3 = 7
    r1 *= -1
    r1 = r1 & r3

    temp2 = r2 >> r1
    r0 = temp1 | temp2
    r0 = (r0 << 0x18) & maxval
    r0 = r0 >> 0x18
    return r0


def _Z9sub_31337hh(r0, r1):
    return r0 ^ r1  # to r0


def _Z10sub_100500h(r0):
    r0 ^= maxval
    r0 = (r0 << 0x18) & maxval
    r0 = (r0 >> 0x18)
    return r0


def alivebeef(r2):
    return ((r2 << 7) + (r2 >> 1)) & 0xFF


def coffee(sym):
    return alivebeef(sym)


flag = [0] * 14
for i in range(14):
    flag[i] = coffee(decoded[i])
    flag[i] = _Z10sub_100500h(flag[i])
    flag[i] = _Z9sub_31337hh(flag[i], mask[i])
    flag[i] = deadbeef(flag[i], 4)

print(''.join(map(chr, flag)))
