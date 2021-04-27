# coding: utf-8

s = raw_input()


def split_words(s):
    words = []
    last_index = 0

    if s.find('-') > 0:
        words = s.split('-')
    elif s.find('_') > 0:
        words = s.split('_')
    else:
        for index, c in enumerate(s[1:]):
            if c >= 'A' and c <= 'Z':
                words.append(s[last_index:index + 1].lower())
                last_index = index + 1

        words.append(s[last_index:].lower())

    return words


def caseTransform(s):
    words = split_words(s)
    first = ''.join([item.title() for item in words])
    second = ''.join([words[0]] + [item.title() for item in words[1:]])
    third = '_'.join([item for item in words])
    fouth = '-'.join([item for item in words])

    return ' '.join([first, second, third, fouth])


print(caseTransform(s))
