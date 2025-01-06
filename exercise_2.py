import re

def fields(string):
    '''
    write a function that returns all of the fields in a haphazardly formatted
    string. a variety of spaces, tabs, and commas separate the fields, with
    possibly multiple occurrences of each delimiter
    '''
    return re.split(r'[ \t,]+', string)



print(fields("Pete,201,Student"));    # ['Pete', '201', 'Student']
print(fields("Pete \t 201   ,  TA")); # ['Pete', '201', 'TA']
print(fields("Pete \t 201"));         # ['Pete', '201']
print(fields("Pete \n 201"));         # ['Pete', '\n', '201']