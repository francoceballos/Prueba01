def save_to_file(content, filename):
    with open(filename, 'w') as fd_save:
        fd_save.write(content)

    return


def read_file(filename):
    with open(filename,'r') as fd_read:
        string = fd_read.read()

    return (string)
