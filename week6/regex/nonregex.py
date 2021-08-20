def is_phone(s):
    """Match phone like 4155551212? """

    return len(s) == 10 and s.isdigit()


def is_phone_dashes(s):
    """Match phone, allowing dashes."""

    if len(s) == 10 and s.isdigit():
        return True

    if (s[3] == "-" and s[7] == "-" and len(s) == 12 and
        s[0:3].isdigit() and s[4:7].isdigit() and s[8:].isdigit()):
        return True

    return False


def is_phone_dashes_intl(s):
    """Match phone, allowing dashes and leading 1."""

    if s.startswith("1-"):
        s = s[2:]

    elif s.startswith("1"):
        s = s[1:]

    if len(s) == 10 and s.isdigit():
        return True

    if (s[3] == "-" and s[7] == "-" and len(s) == 12 and
        s[0:2].isdigit() and s[4:7].isdigit() and s[8:].isdigit()):
        return True

    return False


def is_phone_dashes_intl_ac(s):
    """Match phone, allowing dashes, leading 1, and (area code). """

    if s.startswith("1-"):
        s = s[2:]
    elif s.startswith("1 "):
        s = s[2:]
    elif s.startswith("1"):
        s = s[1:]
    if len(s) == 10 and s.isdigit():
        return True
    if (s[0] == "(" and s[4:6] == ") " and len(s) == 14 and
        s[1:3].isdigit() and s[6:9].isdigit() and s[10:].isdigit()):
        return True
    if (s[3] == "-" and s[7] == "-" and len(s) == 12 and
        s[0:2].isdigit() and s[4:7].isdigit() and s[8:].isdigit()):
        return True
    return False
