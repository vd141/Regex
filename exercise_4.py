import re

def mysterious_math(operation):
    '''
    changes every arithmetic operator to a ? and returns the resulting string
    '''
    return re.sub(r'[\+\-\*\/]', '?', operation)

print(mysterious_math('4 + 3 - 5 = 2'))
# '4 ? 3 ? 5 = 2'

print(mysterious_math('(4 * 3 + 2) / 7 - 1 = 1'))
# '(4 ? 3 ? 2) ? 7 ? 1 = 1'