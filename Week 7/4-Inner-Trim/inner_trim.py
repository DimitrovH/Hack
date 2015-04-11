def drop(string):

    result = ""

    for number in range(1, len(string)):
        result += string[number]

    return result


def trim_left(word):

    result = word

    for ch in word:
        if ch == "!":
            result = drop(word)

    return result


def str_reverse(sth):

    result = ""

    for ch in sth:
        result = ch + result

    return result


def inner_trim(new_string):

    new_string = str_reverse(trim_left(str_reverse(trim_left(new_string))))
    
    result = ""

    for number in range(0, len(new_string) - 1):
        if new_string[number] != "!":
            result += new_string[number]
        elif new_string[number] == "!" and new_string[number + 1] != "!":
                result += new_string[number]

    result += new_string[len(new_string) - 1]

    return result

