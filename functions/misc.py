import math


def to_si(d, sep=' '):
    """
    Convert number to string with SI prefix
    https://stackoverflow.com/a/15734251

    :Example:
    >>> to_si(2500.0)
    '2.5 k'
    >>> to_si(2.3E6)
    '2.3 M'
    >>> to_si(2.3E-6)
    '2.3 µ'
    >>> to_si(-2500.0)
    '-2.5 k'
    >>> to_si(0)
    '0'
    """

    inc_prefixes = ['k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    dec_prefixes = ['m', 'µ', 'n', 'p', 'f', 'a', 'z', 'y']

    if d == 0:
        return str(0)

    degree = int(math.floor(math.log10(math.fabs(d)) / 3))

    prefix = ''

    if degree != 0:
        ds = degree / math.fabs(degree)
        if ds == 1:
            if degree - 1 < len(inc_prefixes):
                prefix = inc_prefixes[degree - 1]
            else:
                prefix = inc_prefixes[-1]
                degree = len(inc_prefixes)

        elif ds == -1:
            if -degree - 1 < len(dec_prefixes):
                prefix = dec_prefixes[-degree - 1]
            else:
                prefix = dec_prefixes[-1]
                degree = -len(dec_prefixes)

        scaled = float(d * math.pow(1000, -degree))

        s = "{scaled}{sep}{prefix}".format(scaled=scaled,
                                           sep=sep,
                                           prefix=prefix)

    else:
        s = "{d}".format(d=d)

    return s
