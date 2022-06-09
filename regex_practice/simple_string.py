import re
#this is a simple function for recognizing patterns in texts
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""
    p = '([A-Z]+[a-z$]+)'
    return re.findall(p,simple_string)
names()