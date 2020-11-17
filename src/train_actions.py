import sys


def simple_function(x):
    if type(x) is str:
        return True
    else:
        return False


if len(sys.argv) == 2:
    print(simple_function(sys.argv[1]))
else:
    print("plz specify at one.")
