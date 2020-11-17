import sys


def simple_function(x):
    if type(x) is str:
        print("it's strings.")
    else:
        print("not strings.")


if len(sys.argv) == 2:
    simple_function(sys.argv[1])
else:
    print("plz specify at one.")
