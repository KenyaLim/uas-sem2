
def hurufJagaJarak(string):
    if len(string) == 1:
        return string
    if string[0] == string[1]:
        return hurufJagaJarak(string[1:])
    return string[0] + hurufJagaJarak(string[1:])
