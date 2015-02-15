import os

def file_in(filename="input.txt"):
    """ Gets an input file and returns its contents or None """
    if os.path.exists(filename):
        with open(filename, mode='r') as fh:
            contents = fh.read()
        return contents
    else:
        return None

def file_out(data, filename="output.txt"):
    """ Dumps the data into a file. """
    with open(filename, mode='w') as fh:
        if is_sequence(data):
            for item in data:
                print(item, file=fh)
        else:
            print(data, file=fh)

def is_sequence(obj):
    """ Checks if an object is a sequence but not a string. """
    return (not hasattr(obj, "strip") and (hasattr(obj, "__getitem__") or hasattr(obj, "__iter__")))
