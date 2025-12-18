def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        rev = ""
        for ch in s:
            rev = ch + rev
        return rev
    else:
        return s
