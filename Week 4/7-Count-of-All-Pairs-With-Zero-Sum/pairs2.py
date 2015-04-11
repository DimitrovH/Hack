def count_zero_pairs(numbers):

    result = 0
    end = len(numbers)

    for x in range(0, end):
        for y in range(x, end):
            if numbers[x] + numbers[y] == 0:
                result += 1

    return result

print(count_zero_pairs([0, 2, -2, 5,]))


