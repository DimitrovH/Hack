def count_zero_neighbours(numbers):

    result = 0
    index = 0
    end = len(numbers) - 1

    for number in numbers:
        if index < end and numbers[index] + numbers[index + 1] == 0:
            result += 1
        index += 1

    return result

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))