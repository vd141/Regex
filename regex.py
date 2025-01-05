import re

def p(text):
    print(re.findall(r'^c.t',
                     text,
                     flags=re.IGNORECASE))

p("cat")         # ['cat']
p("cot\n")       # ['cot']
p("CATASTROPHE") # ['CAT']
p("WILDCAUGHT")  # []
p("wildcat\n")   # []
p("-CET-")       # []
p("Yacht")       # []