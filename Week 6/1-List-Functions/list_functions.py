def head(items):

    return items[0]

def last(items):
    last_index = len(items) - 1
    
    return items[last_index]

def tail(items):

    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]

    return result

def equal_lists(l1, l2):
    if len(l1) != len(l2):
        return False

    while len(l1) != 0:
        if head(l1) != head(l2):
            return False

        l1 = tail(l1)
        l2 = tail(l2)

    return True

def count_item(item, list1):

    count = 0

    for x in list1:
        if x == item:
            count += 1

    return count

def take(n, list1):

    list2 = []

    for index in range(0, min(n, len(list1))):
        list2 += [list1[index]]

    return list2

def drop(n, items):

    result = []

    for index in range(n, len(items)):
        result += [items[index]]

    return result

def reverse(items):
	
    result = []

    last_index = len(items) - 1

    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1

    return result

