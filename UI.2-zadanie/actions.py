
# kontrola pohybu hore a doprava, ci neprekracujem mapu a ci je dane policko volne
def up_right(value, index, x, y,n):
    if y - 2 >= 0 and x + 1 < n and value[index - 2 * n + 1] == 0:
        return True
    return False


# kontrola pohuby hore a dolava
def up_left(value, index, x, y,n):
    if y - 2 >= 0 and x - 1 >= 0 and value[index - 2 * n - 1] == 0:
        return True
    return False


# kontrola pohybu vlavo a hore
def left_up(value, index, x, y,n):
    if y - 1 >= 0 and x - 2 >= 0 and value[index - n - 2] == 0:
        return True
    return False


# kontrola pohybu vlavo a dole
def left_down(value, index, x, y,n):
    if y + 1 < n and x - 2 >= 0 and value[index + n - 2] == 0:
        return True
    return False


# kontrola pohybu vpravo a hore
def right_up(value, index, x, y,n):
    if y - 1 >= 0 and x + 2 < n and value[index - n + 2] == 0:
        return True
    return False


# kontrola pohybu vpravo a hore
def right_down(value, index, x, y,n):
    if y + 1 < n and x + 2 < n and value[index + n + 2] == 0:
        return True
    return False


# kontrola pohybu dole a vlavo
def down_left(value, index, x, y,n):
    if y + 2 < n and x - 1 >= 0 and value[index + 2 * n - 1] == 0:
        return True
    return False


# kontrola pohybu dole a vpravo
def down_right(value, index, x, y,n):
    if y + 2 < n and x + 1 < n and value[index + 2 * n + 1] == 0:
        return True
    return False