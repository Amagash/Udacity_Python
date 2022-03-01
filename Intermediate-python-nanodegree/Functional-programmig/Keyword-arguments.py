"""
Keyword arguments, also known as default arguments, named arguments, or optional arguments. are a mechanism for providing a default value 
for one or more parameters. An argument can be supplied either (1) by position or (2) by keyword
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

if __name__ == '__main__':
    parrot(1000)
    parrot(voltage=1000)
    parrot(voltage=1000000, action='VOOOOOM')
    parrot(action='VOOOOOM', voltage=1000000)
    parrot('a million', 'bereft of life', 'jump')
    parrot('a thousand', state='pushing up the daisies')