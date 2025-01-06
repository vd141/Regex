import re

def is_url(string):
    '''
    returns true if the argument looks like a URL, false otherwise
    '''
    regexp = r'^https?://.*.com$'
    return True if re.match(regexp, string) else False

print(is_url('https://launchschool.com'))    # -> true
print(is_url('http://example.com'))          # -> true
print(is_url('https://example.com hello'))   # -> false
print(is_url('   https://example.com'))      # -> false