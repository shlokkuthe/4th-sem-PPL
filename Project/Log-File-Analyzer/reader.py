def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines