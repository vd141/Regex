import re

def mystery_math(operation):
    '''
    function that changes the first arithmetic operator (+-*/) in a string to a ?
    and returns the resulting string. don't modify the original string
    '''
    return re.sub(r'[\+\-\*\/]', '?', operation, count=1)

print(mystery_math('4 + 3 - 5 = 2'))
# '4 ? 3 - 5 = 2'

print(mystery_math('(4 * 3 + 2) / 7 - 1 = 1'))
# '(4 ? 3 + 2) / 7 - 1 = 1'