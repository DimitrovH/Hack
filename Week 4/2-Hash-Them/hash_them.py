def hash_them(keys, values):
    result = {}
    end = len(values)

    index = 0

    for key in keys:
        if index < end:
            result[key] = values[index]
        else:
            result[key] = None

        index += 1

    
    return result

print(hash_them(["Ivan", "Maria", "Petko"], [1, 2]))
