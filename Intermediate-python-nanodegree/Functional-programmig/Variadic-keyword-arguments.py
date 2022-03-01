"""
A variadic parameter collection collects excess arguments (that would otherwise go unmatched to a parameter) into a data structure, 
for the function implementation's use. 
There are two kinds of variadic parameters: variadic positional parameters (*) and variadic keyword parameters (**).
"""

def print_my_arguments(a, b=1, **c):
    print(f"a={a}, b={b}, c={c}")

def authorize(quote, **speaker_info):
    print(">", quote)
    print("-" * (len(quote) + 2))
    for key, value in speaker_info.items():
        print(key, value, sep=': ')

if __name__ == '__main__':
    print_my_arguments(2)                      # a=2, b=1, c={}
    print_my_arguments(2, x=7)                 # a=2, b=1, c={'x': 7}
    print_my_arguments(2, x=7, y=1)            # a=2, b=1, c={'x': 7, 'y': 1}
    print_my_arguments(2, x=7, y=1, z=8)       # a=2, b=1, c={'x': 7, 'y': 1, 'z': 8}
    print_my_arguments(2, x=7, y=1, z=8, b=2)  # a=2, b=2, c={'x': 7, 'y': 1, 'z': 8}
    print_my_arguments(2, x=7, b=2, y=1, z=8)  # a=2, b=2, c={'x': 7, 'y': 1, 'z': 8}

    authorize(
    "If music be the food of love, play on.",
    playwright="Shakespeare",
    act=1,
    scene=1,
    speaker="Duke Orsino"
    )

    authorize(
        "O partigiano, portami via.",
        canzone="Bella Ciao",
        lingua="Italiano",
    )

    info = {
    'sonnet': 18,
    'line': 1,
    'author': "Shakespeare"
    }
    authorize("Shall I compare thee to a summer's day", **info)