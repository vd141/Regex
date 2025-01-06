import re

def danish(sentence):
    '''
    function that changes the first occurrence of the word apple, blueberry, or
    cherry in a string to danish
    '''

    return re.sub(r'\b(apple|blueberry|cherry)\b', 'danish', sentence, count=1)

print(danish('An apple a day keeps the doctor away'))
# -> 'An danish a day keeps the doctor away'

print(danish('My favorite is blueberry pie'))
# -> 'My favorite is danish pie'

print(danish('The cherry of my eye'))
# -> 'The danish of my eye'

print(danish('apple. cherry. blueberry.'))
# -> 'danish. cherry. blueberry.'

print(danish('I love pineapple'))
# -> 'I love pineapple'

print(danish('appleberry'))
