def display_hex(func):
    def _display_hex():
        ret = func()
        return hex(ret)
    return _display_hex

@display_hex
def numer():
    return 45

print numer()