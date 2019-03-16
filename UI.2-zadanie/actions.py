
def up_right(value, index, x, y,n):
    """ kontrola pohybu hore a doprava, ci neprekracujem mapu a ci je dane policko volne"""
    if y - 2 >= 0 and x + 1 < n and value[index - 2 * n + 1] == 0:
        return True
    return False


def up_left(value, index, x, y,n):
    """ kontrola pohuby hore a dolava"""
    if y - 2 >= 0 and x - 1 >= 0 and value[index - 2 * n - 1] == 0:
        return True
    return False


def left_up(value, index, x, y,n):
    """ kontrola pohybu vlavo a hore"""
    if y - 1 >= 0 and x - 2 >= 0 and value[index - n - 2] == 0:
        return True
    return False


def left_down(value, index, x, y,n):
    """ kontrola pohybu vlavo a dole"""
    if y + 1 < n and x - 2 >= 0 and value[index + n - 2] == 0:
        return True
    return False


def right_up(value, index, x, y,n):
    """ kontrola pohybu vpravo a hore"""
    if y - 1 >= 0 and x + 2 < n and value[index - n + 2] == 0:
        return True
    return False


def right_down(value, index, x, y,n):
    """ kontrola pohybu vpravo a hore"""
    if y + 1 < n and x + 2 < n and value[index + n + 2] == 0:
        return True
    return False


def down_left(value, index, x, y,n):
    """ kontrola pohybu dole a vlavo"""
    if y + 2 < n and x - 1 >= 0 and value[index + 2 * n - 1] == 0:
        return True
    return False


def down_right(value, index, x, y,n):
    """ kontrola pohybu dole a vpravo"""
    if y + 2 < n and x + 1 < n and value[index + 2 * n + 1] == 0:
        return True
    return False