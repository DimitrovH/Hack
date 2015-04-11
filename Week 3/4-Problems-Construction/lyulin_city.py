def solution(blocks):
    if len(blocks) == 0:
        return 0

    result = 1
    current_max = blocks[0]

    for block in blocks:
        if block > current_max:
            result += 1
            current_max = block

    return result

n = input()
n = int(n)

blocks = []
start = 0

while start < n:
    height = input()
    heihgt = int(height)

    blocks = blocks + [height]

    start += 1

print(solution(blocks))