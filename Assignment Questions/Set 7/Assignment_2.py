def remove_duplicates(value):
    newVal = set(list(value))
    value = list(value)
    value = value[::-1]
    for i in newVal:
        while value.count(i) != 1:
            value.remove(i)
    return "".join(value[::-1])
print(remove_duplicates("1122334455ababzzz@@@123#*#*"))