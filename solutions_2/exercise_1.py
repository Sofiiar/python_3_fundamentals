def reassign_if_none(value):
    if value is None:
        value = "N/A"
    return value


a = None
a = reassign_if_none(a)
print(a)

a = 5
a = reassign_if_none(a)
print(a)

