def reassign_if_none(value):
    return "N/A" if value is None else value


a = None
a = reassign_if_none(a)
print(a)

a = 5
a = reassign_if_none(a)
print(a)
